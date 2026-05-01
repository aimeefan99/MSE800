"""
Transaction Manager Module for Money Exchange System
====================================================
This module provides all business logic functions for managing:
- Customers (add, view, search)
- Accounts (create, link customers, view)
- Transactions (currency exchange, view history)
- Currencies and Banks (view available options)

All functions interact with the SQLite database through the database module.
"""

from database import create_connection
import sqlite3

# ==================== CUSTOMER MANAGEMENT ====================

def add_customer(full_name, email, phone, passport_no):
    """
    Add a new customer to the system
    
    Args:
        full_name (str): Customer's full legal name
        email (str): Customer's email address (must be unique)
        phone (str): Customer's contact phone number
        passport_no (str): Customer's passport number for KYC compliance (must be unique)
    
    Returns:
        int: The new customer's ID if successful, None if failed
    
    Note:
        Email and Passport_No must be unique. Duplicate entries will be rejected.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO CUSTOMER (Full_Name, Email, Phone, Passport_No) VALUES (?, ?, ?, ?)",
            (full_name, email, phone, passport_no)
        )
        conn.commit()
        print(f"✅ Customer '{full_name}' added successfully! (ID: {cursor.lastrowid})")
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f"❌ Error: {e}")
        return None
    finally:
        conn.close()

def view_customers():
    """
    View all customers in the system
    
    Returns:
        list: List of tuples containing customer information
              (Customer_ID, Full_Name, Email, Phone, Passport_No)
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CUSTOMER")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==================== ACCOUNT MANAGEMENT ====================

def create_account(bank_id, account_type, initial_balance=0.0):
    """
    Create a new account in the system
    
    Args:
        bank_id (int): ID of the bank managing this account
        account_type (str): Type of account (e.g., 'Savings', 'Checking', 'Joint')
        initial_balance (float): Starting balance for the account (default: 0.0)
    
    Returns:
        int: The new account number if successful, None if failed
    
    Note:
        After creating an account, you must link at least one customer to it
        using the link_customer_to_account() function.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ACCOUNT (Bank_ID, Account_Type, Balance) VALUES (?, ?, ?)",
            (bank_id, account_type, initial_balance)
        )
        conn.commit()
        account_no = cursor.lastrowid
        print(f"✅ Account created successfully! (Account No: {account_no})")
        return account_no
    except sqlite3.Error as e:
        print(f"❌ Error creating account: {e}")
        return None
    finally:
        conn.close()

def link_customer_to_account(account_no, customer_id, role='Owner'):
    """
    Link a customer to an account (enables joint accounts)
    
    This function implements the M:N relationship between customers and accounts.
    Multiple customers can be linked to the same account (joint account).
    
    Args:
        account_no (int): The account number to link
        customer_id (int): The customer ID to link
        role (str): Customer's role in the account (default: 'Owner')
                   Options: 'Owner', 'Co-Owner', 'Authorized'
    
    Returns:
        bool: True if successful, False if customer is already linked
    
    Example:
        # Create a joint account for Alice and Bob
        link_customer_to_account(1003, 1, 'Owner')      # Alice as Owner
        link_customer_to_account(1003, 2, 'Co-Owner')   # Bob as Co-Owner
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ACCOUNT_CUSTOMER (Account_No, Customer_ID, Role) VALUES (?, ?, ?)",
            (account_no, customer_id, role)
        )
        conn.commit()
        print(f"✅ Customer {customer_id} linked to Account {account_no} as {role}")
        return True
    except sqlite3.IntegrityError:
        print(f"❌ Customer {customer_id} is already linked to Account {account_no}")
        return False
    finally:
        conn.close()

def view_accounts():
    """
    View all accounts with their owners
    
    Returns:
        list: List of tuples containing:
              (Account_No, Account_Type, Balance, Bank_Name, Owners)
              where Owners is a comma-separated list of customer names with their roles
    
    Note:
        Uses SQL JOIN and GROUP_CONCAT to show all owners of joint accounts
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            A.Account_No,
            A.Account_Type,
            A.Balance,
            B.Bank_Name,
            GROUP_CONCAT(C.Full_Name || ' (' || AC.Role || ')', ', ') as Owners
        FROM ACCOUNT A
        JOIN BANK B ON A.Bank_ID = B.Bank_ID
        LEFT JOIN ACCOUNT_CUSTOMER AC ON A.Account_No = AC.Account_No
        LEFT JOIN CUSTOMER C ON AC.Customer_ID = C.Customer_ID
        GROUP BY A.Account_No
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_customer_accounts(customer_id):
    """
    View all accounts for a specific customer
    
    Args:
        customer_id (int): The customer's ID
    
    Returns:
        list: List of tuples containing:
              (Account_No, Account_Type, Balance, Bank_Name, Role)
              showing all accounts the customer has access to
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            A.Account_No,
            A.Account_Type,
            A.Balance,
            B.Bank_Name,
            AC.Role
        FROM ACCOUNT A
        JOIN BANK B ON A.Bank_ID = B.Bank_ID
        JOIN ACCOUNT_CUSTOMER AC ON A.Account_No = AC.Account_No
        WHERE AC.Customer_ID = ?
    ''', (customer_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==================== TRANSACTION MANAGEMENT ====================

def make_transaction(account_no, currency_code, amount):
    """
    Record a currency exchange transaction
    
    This function:
    1. Validates the account exists and has sufficient balance
    2. Retrieves the currency exchange rate
    3. Calculates the converted amount
    4. Records the transaction
    5. Updates the account balance
    
    Args:
        account_no (int): The account number to debit from
        currency_code (str): Target currency code (e.g., 'USD', 'EUR')
        amount (float): Amount in NZD to exchange
    
    Returns:
        bool: True if transaction successful, False otherwise
    
    Example:
        # Exchange 1000 NZD to USD
        make_transaction(1001, 'USD', 1000.0)
        # This will deduct 1000 NZD and show equivalent USD amount
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Step 1: Check if account exists and get current balance
        cursor.execute("SELECT Balance FROM ACCOUNT WHERE Account_No = ?", (account_no,))
        result = cursor.fetchone()
        
        if not result:
            print(f"❌ Account {account_no} not found!")
            return False
        
        current_balance = result[0]
        
        # Step 2: Get currency rate and symbol
        cursor.execute("SELECT Rate, Symbol FROM CURRENCY WHERE Currency_Code = ?", (currency_code,))
        currency_result = cursor.fetchone()
        
        if not currency_result:
            print(f"❌ Currency {currency_code} not found!")
            return False
        
        rate, symbol = currency_result
        converted_amount = amount * rate
        
        # Step 3: Validate sufficient balance
        if current_balance < amount:
            print(f"❌ Insufficient balance! Current: ${current_balance:.2f}, Required: ${amount:.2f}")
            return False
        
        # Step 4: Record transaction in TRANSACTION table
        cursor.execute(
            'INSERT INTO "TRANSACTION" (Account_No, Currency_Code, Amount) VALUES (?, ?, ?)',
            (account_no, currency_code, amount)
        )
        
        # Step 5: Update account balance (deduct the exchanged amount)
        new_balance = current_balance - amount
        cursor.execute(
            "UPDATE ACCOUNT SET Balance = ? WHERE Account_No = ?",
            (new_balance, account_no)
        )
        
        conn.commit()
        print(f"✅ Transaction successful!")
        print(f"   Exchanged: ${amount:.2f} NZD → {symbol}{converted_amount:.2f} {currency_code}")
        print(f"   New Balance: ${new_balance:.2f}")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Transaction failed: {e}")
        conn.rollback()  # Rollback changes if any error occurs
        return False
    finally:
        conn.close()

def view_transactions(account_no=None):
    """
    View transaction history
    
    Args:
        account_no (int, optional): If provided, shows transactions for specific account only.
                                   If None, shows all transactions in the system.
    
    Returns:
        list: List of tuples containing:
              (Trans_ID, Account_No, Currency_Code, Amount, Trans_Date, Symbol, Rate)
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    if account_no:
        # Get transactions for specific account
        cursor.execute('''
            SELECT 
                T.Trans_ID,
                T.Account_No,
                T.Currency_Code,
                T.Amount,
                T.Trans_Date,
                C.Symbol,
                C.Rate
            FROM "TRANSACTION" T
            JOIN CURRENCY C ON T.Currency_Code = C.Currency_Code
            WHERE T.Account_No = ?
            ORDER BY T.Trans_Date DESC
        ''', (account_no,))
    else:
        # Get all transactions
        cursor.execute('''
            SELECT 
                T.Trans_ID,
                T.Account_No,
                T.Currency_Code,
                T.Amount,
                T.Trans_Date,
                C.Symbol,
                C.Rate
            FROM "TRANSACTION" T
            JOIN CURRENCY C ON T.Currency_Code = C.Currency_Code
            ORDER BY T.Trans_Date DESC
        ''')
    
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==================== CURRENCY MANAGEMENT ====================

def view_currencies():
    """
    View all available currencies for exchange
    
    Returns:
        list: List of tuples containing:
              (Currency_Code, Name, Symbol, Rate, Active)
              Only returns currencies where Active = 1
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CURRENCY WHERE Active = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_banks():
    """
    View all banks in the system
    
    Returns:
        list: List of tuples containing:
              (Bank_ID, Bank_Name, Swift_Code, Branch_Code, Country)
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BANK")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ==================== DEPOSIT FUNCTION ====================

def deposit_to_account(account_no, amount):
    """
    Deposit money to an account
    
    Args:
        account_no (int): The account number to deposit to
        amount (float): Amount to deposit (must be positive)
    
    Returns:
        bool: True if deposit successful, False otherwise
    
    Note:
        This function only adds money to the account balance.
        It does not create a transaction record.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Check if account exists
        cursor.execute("SELECT Balance FROM ACCOUNT WHERE Account_No = ?", (account_no,))
        result = cursor.fetchone()
        
        if not result:
            print(f"❌ Account {account_no} not found!")
            return False
        
        # Calculate new balance and update
        new_balance = result[0] + amount
        cursor.execute("UPDATE ACCOUNT SET Balance = ? WHERE Account_No = ?", (new_balance, account_no))
        conn.commit()
        print(f"✅ Deposited ${amount:.2f}. New balance: ${new_balance:.2f}")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Deposit failed: {e}")
        return False
    finally:
        conn.close()

# Made with Bob
