"""
Database Module for Money Exchange System
==========================================
This module handles database connection and table creation for the currency exchange application.
It implements a Many-to-Many (M:N) relationship between CUSTOMER and ACCOUNT using a junction table.

Database Schema:
- BANK: Stores banking institution information
- CUSTOMER: Stores customer personal information  
- CURRENCY: Stores supported currencies and exchange rates
- ACCOUNT: Stores account information (linked to banks)
- ACCOUNT_CUSTOMER: Junction table for M:N relationship (supports joint accounts)
- TRANSACTION: Stores currency exchange transaction records
"""

import sqlite3

def create_connection():
    """
    Create a database connection to the money_exchange.db database
    
    Returns:
        sqlite3.Connection: Database connection object
    """
    conn = sqlite3.connect("money_exchange.db")
    return conn

def create_tables():
    """
    Create all tables for the Money Exchange system
    
    This function creates 6 tables with proper relationships:
    1. BANK - Stores banking institution information
    2. CUSTOMER - Stores customer personal information
    3. CURRENCY - Stores supported currencies and exchange rates
    4. ACCOUNT - Stores account information (linked to banks)
    5. ACCOUNT_CUSTOMER - Junction table for M:N relationship (supports joint accounts)
    6. TRANSACTION - Stores currency exchange transaction records
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    # ==================== BANK TABLE ====================
    # Stores information about financial institutions
    # Each bank has a unique SWIFT code for international identification
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BANK (
            Bank_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Bank_Name TEXT NOT NULL,
            Swift_Code TEXT NOT NULL UNIQUE,
            Branch_Code TEXT NOT NULL,
            Country TEXT NOT NULL
        )
    ''')
    
    # ==================== CUSTOMER TABLE ====================
    # Stores customer identity and contact information
    # Email and Passport_No are UNIQUE to ensure data integrity and prevent duplicates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CUSTOMER (
            Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Full_Name TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE,
            Phone TEXT NOT NULL,
            Passport_No TEXT NOT NULL UNIQUE
        )
    ''')
    
    # ==================== CURRENCY TABLE ====================
    # Defines supported currencies and their exchange rates
    # Currency_Code is the PRIMARY KEY (e.g., 'USD', 'EUR', 'NZD')
    # Rate represents the exchange rate relative to NZD (base currency)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CURRENCY (
            Currency_Code TEXT PRIMARY KEY,
            Name TEXT NOT NULL,
            Symbol TEXT NOT NULL,
            Rate REAL NOT NULL,
            Active INTEGER NOT NULL DEFAULT 1
        )
    ''')
    
    # ==================== ACCOUNT TABLE ====================
    # Stores account information
    # IMPORTANT: Customer_ID is NOT here because we use M:N relationship via ACCOUNT_CUSTOMER table
    # This design supports joint accounts (multiple customers per account)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACCOUNT (
            Account_No INTEGER PRIMARY KEY AUTOINCREMENT,
            Bank_ID INTEGER NOT NULL,
            Account_Type TEXT NOT NULL,
            Balance REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (Bank_ID) REFERENCES BANK(Bank_ID)
        )
    ''')
    
    # ==================== ACCOUNT_CUSTOMER JUNCTION TABLE ====================
    # Implements Many-to-Many (M:N) relationship between CUSTOMER and ACCOUNT
    # This table allows:
    # - One customer to have multiple accounts
    # - One account to have multiple customers (joint/family accounts)
    # Role field indicates the customer's relationship to the account (Owner/Co-Owner/Authorized)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACCOUNT_CUSTOMER (
            Account_No INTEGER NOT NULL,
            Customer_ID INTEGER NOT NULL,
            Role TEXT DEFAULT 'Owner',
            Join_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (Account_No, Customer_ID),
            FOREIGN KEY (Account_No) REFERENCES ACCOUNT(Account_No),
            FOREIGN KEY (Customer_ID) REFERENCES CUSTOMER(Customer_ID)
        )
    ''')
    
    # ==================== TRANSACTION TABLE ====================
    # Records all currency exchange transactions
    # NOTE: "TRANSACTION" is quoted because TRANSACTION is a SQL reserved keyword
    # Each transaction is linked to an account and a target currency
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "TRANSACTION" (
            Trans_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Account_No INTEGER NOT NULL,
            Currency_Code TEXT NOT NULL,
            Amount REAL NOT NULL,
            Trans_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (Account_No) REFERENCES ACCOUNT(Account_No),
            FOREIGN KEY (Currency_Code) REFERENCES CURRENCY(Currency_Code)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database tables created successfully!")

def initialize_sample_data():
    """
    Insert sample data for testing and demonstration
    
    This function populates the database with:
    - 3 banks (ANZ, ASB, Westpac) - Major New Zealand banks
    - 5 currencies (NZD, USD, EUR, GBP, AUD) - Common trading currencies
    - 3 sample customers (Alice, Bob, Candy) - Test users
    - 3 sample accounts (including one joint account) - Demonstrates different account types
    - Account-Customer relationships - Shows how joint accounts work
    
    Uses INSERT OR IGNORE to prevent duplicate entries on subsequent runs
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # ==================== INSERT SAMPLE BANKS ====================
        # Three major NZ banks with their SWIFT codes and branch information
        cursor.execute('''
            INSERT OR IGNORE INTO BANK (Bank_Name, Swift_Code, Branch_Code, Country)
            VALUES
                ('ANZ Bank', 'ANZBNZ22', 'AKL001', 'New Zealand'),
                ('ASB Bank', 'ASBBNZ2A', 'WLG001', 'New Zealand'),
                ('Westpac', 'WPACNZ2W', 'CHC001', 'New Zealand')
        ''')
        
        # ==================== INSERT SAMPLE CURRENCIES ====================
        # Five major currencies with exchange rates relative to NZD (base currency = 1.0)
        # Rate represents how much of the currency equals 1 NZD
        # Example: USD rate of 0.62 means 1 NZD = 0.62 USD
        cursor.execute('''
            INSERT OR IGNORE INTO CURRENCY (Currency_Code, Name, Symbol, Rate, Active)
            VALUES
                ('NZD', 'New Zealand Dollar', '$', 1.0, 1),
                ('USD', 'US Dollar', '$', 0.62, 1),
                ('EUR', 'Euro', '€', 0.57, 1),
                ('GBP', 'British Pound', '£', 0.49, 1),
                ('AUD', 'Australian Dollar', '$', 0.94, 1)
        ''')
        
        # ==================== INSERT SAMPLE CUSTOMERS ====================
        # Three test customers with complete KYC (Know Your Customer) information
        # Each has unique email and passport number for identification
        cursor.execute('''
            INSERT OR IGNORE INTO CUSTOMER (Customer_ID, Full_Name, Email, Phone, Passport_No)
            VALUES
                (1, 'Alice', 'alice@gmail.com', '027122345', 'AA12345'),
                (2, 'Bob', 'bob@gmail.com', '02754321', 'BB54321'),
                (3, 'Candy', 'candy@gmail.com', '027334455', 'CC334455')
        ''')
        
        # ==================== INSERT SAMPLE ACCOUNTS ====================
        # Three accounts across different banks and types
        # Account 1001: Alice's personal savings account at ANZ
        # Account 1002: Bob's personal checking account at ASB  
        # Account 1003: Joint account at ANZ (will be shared by Alice and Bob)
        cursor.execute('''
            INSERT OR IGNORE INTO ACCOUNT (Account_No, Bank_ID, Account_Type, Balance)
            VALUES
                (1001, 1, 'Savings', 5000.00),
                (1002, 2, 'Checking', 3000.00),
                (1003, 1, 'Joint', 10000.00)
        ''')
        
        # ==================== LINK CUSTOMERS TO ACCOUNTS ====================
        # Demonstrates the M:N relationship through the junction table
        # Alice: Owns account 1001 (personal) and co-owns account 1003 (joint)
        # Bob: Owns account 1002 (personal) and co-owns account 1003 (joint)
        # This shows how joint accounts work - multiple customers can access the same account
        cursor.execute('''
            INSERT OR IGNORE INTO ACCOUNT_CUSTOMER (Account_No, Customer_ID, Role)
            VALUES
                (1001, 1, 'Owner'),
                (1002, 2, 'Owner'),
                (1003, 1, 'Owner'),
                (1003, 2, 'Co-Owner')
        ''')
        
        conn.commit()
        print("✅ Sample data initialized!")
    except sqlite3.IntegrityError:
        print("ℹ️  Sample data already exists.")
    finally:
        conn.close()

# Made with Bob
