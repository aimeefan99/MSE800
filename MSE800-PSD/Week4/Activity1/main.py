"""
Main Application Module for Money Exchange System
=================================================
This is the main entry point for the Money Exchange Management System.
It provides an interactive command-line interface for:
- Customer Management (add, view, search customers)
- Account Management (create accounts, link customers, deposits)
- Transaction Management (currency exchange, view history)
- Information Viewing (banks, currencies, accounts)

The application uses a menu-driven interface with multiple submenus
for different functional areas.
"""

from database import create_tables, initialize_sample_data
from transaction_manager import (
    add_customer, view_customers, view_customer_accounts,
    create_account, link_customer_to_account, view_accounts,
    make_transaction, view_transactions,
    view_currencies, view_banks, deposit_to_account
)

def print_header(title):
    """
    Print a formatted section header
    
    Args:
        title (str): The title text to display in the header
    """
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)

def main_menu():
    """
    Display the main menu of the application
    
    Shows 5 main options:
    1. Customer Management - Add and manage customers
    2. Account Management - Create and manage accounts
    3. Transaction Management - Perform currency exchanges
    4. View Information - View system data
    5. Exit - Close the application
    """
    print("\n╔════════════════════════════════════════════════╗")
    print("║     💰 Money Exchange Management System 💰     ║")
    print("╚════════════════════════════════════════════════╝")
    print("\n📋 MAIN MENU:")
    print("  1. Customer Management")
    print("  2. Account Management")
    print("  3. Transaction Management")
    print("  4. View Information")
    print("  5. Exit")
    print("-" * 50)

def customer_menu():
    """
    Customer management submenu
    
    Provides options to:
    - Add new customers with KYC information
    - View all customers in the system
    - View accounts belonging to a specific customer
    - Return to main menu
    """
    while True:
        print_header("👤 CUSTOMER MANAGEMENT")
        print("  1. Add New Customer")
        print("  2. View All Customers")
        print("  3. View Customer's Accounts")
        print("  4. Back to Main Menu")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            print("\n➕ Add New Customer")
            name = input("Full Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            passport = input("Passport No: ").strip()
            add_customer(name, email, phone, passport)
            
        elif choice == '2':
            print("\n📋 All Customers:")
            customers = view_customers()
            if customers:
                print(f"\n{'ID':<5} {'Name':<25} {'Email':<30} {'Phone':<15} {'Passport':<15}")
                print("-" * 90)
                for c in customers:
                    print(f"{c[0]:<5} {c[1]:<25} {c[2]:<30} {c[3]:<15} {c[4]:<15}")
            else:
                print("No customers found.")
                
        elif choice == '3':
            customer_id = input("\nEnter Customer ID: ").strip()
            if customer_id.isdigit():
                accounts = view_customer_accounts(int(customer_id))
                if accounts:
                    print(f"\n📋 Accounts for Customer ID {customer_id}:")
                    print(f"\n{'Account No':<12} {'Type':<15} {'Balance':<12} {'Bank':<20} {'Role':<10}")
                    print("-" * 70)
                    for acc in accounts:
                        print(f"{acc[0]:<12} {acc[1]:<15} ${acc[2]:<11.2f} {acc[3]:<20} {acc[4]:<10}")
                else:
                    print(f"No accounts found for Customer ID {customer_id}")
            else:
                print("❌ Invalid Customer ID")
                
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice. Please try again.")

def account_menu():
    """
    Account management submenu
    
    Provides options to:
    - Create new accounts (linked to banks)
    - Link customers to accounts (enables joint accounts)
    - View all accounts with their owners
    - Deposit money to accounts
    - Return to main menu
    
    Note: This menu demonstrates the M:N relationship between customers and accounts
    """
    while True:
        print_header("🏦 ACCOUNT MANAGEMENT")
        print("  1. Create New Account")
        print("  2. Link Customer to Account (Joint Account)")
        print("  3. View All Accounts")
        print("  4. Deposit to Account")
        print("  5. Back to Main Menu")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            print("\n➕ Create New Account")
            
            # Show available banks
            banks = view_banks()
            print("\nAvailable Banks:")
            for bank in banks:
                print(f"  {bank[0]}. {bank[1]} ({bank[2]})")
            
            bank_id = input("\nEnter Bank ID: ").strip()
            account_type = input("Account Type (Savings/Checking/Joint): ").strip()
            initial_balance = input("Initial Balance (default 0): ").strip()
            
            if bank_id.isdigit():
                balance = float(initial_balance) if initial_balance else 0.0
                account_no = create_account(int(bank_id), account_type, balance)
                
                if account_no:
                    # Link customer to account
                    customer_id = input("\nEnter Customer ID to link to this account: ").strip()
                    if customer_id.isdigit():
                        link_customer_to_account(account_no, int(customer_id), 'Owner')
            else:
                print("❌ Invalid Bank ID")
                
        elif choice == '2':
            print("\n🔗 Link Customer to Account")
            account_no = input("Enter Account Number: ").strip()
            customer_id = input("Enter Customer ID: ").strip()
            role = input("Role (Owner/Co-Owner/Authorized): ").strip() or "Co-Owner"
            
            if account_no.isdigit() and customer_id.isdigit():
                link_customer_to_account(int(account_no), int(customer_id), role)
            else:
                print("❌ Invalid input")
                
        elif choice == '3':
            print("\n📋 All Accounts:")
            accounts = view_accounts()
            if accounts:
                print(f"\n{'Account No':<12} {'Type':<15} {'Balance':<12} {'Bank':<20} {'Owners':<40}")
                print("-" * 100)
                for acc in accounts:
                    owners = acc[4] if acc[4] else "No owners linked"
                    print(f"{acc[0]:<12} {acc[1]:<15} ${acc[2]:<11.2f} {acc[3]:<20} {owners:<40}")
            else:
                print("No accounts found.")
                
        elif choice == '4':
            print("\n💵 Deposit to Account")
            account_no = input("Enter Account Number: ").strip()
            amount = input("Enter Amount to Deposit: ").strip()
            
            if account_no.isdigit() and amount:
                try:
                    deposit_to_account(int(account_no), float(amount))
                except ValueError:
                    print("❌ Invalid amount")
            else:
                print("❌ Invalid input")
                
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice. Please try again.")

def transaction_menu():
    """
    Transaction management submenu
    
    Provides options to:
    - Make currency exchange transactions
    - View all transactions in the system
    - View transactions for a specific account
    - Return to main menu
    
    Note: Transactions deduct from account balance and record exchange details
    """
    while True:
        print_header("💱 TRANSACTION MANAGEMENT")
        print("  1. Make Currency Exchange")
        print("  2. View All Transactions")
        print("  3. View Account Transactions")
        print("  4. Back to Main Menu")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            print("\n💱 Currency Exchange")
            
            # Show available currencies
            currencies = view_currencies()
            print("\nAvailable Currencies:")
            print(f"\n{'Code':<8} {'Name':<25} {'Symbol':<8} {'Rate (to NZD)':<15}")
            print("-" * 60)
            for curr in currencies:
                print(f"{curr[0]:<8} {curr[1]:<25} {curr[2]:<8} {curr[3]:<15.4f}")
            
            account_no = input("\nEnter Account Number: ").strip()
            currency_code = input("Enter Currency Code (e.g., USD, EUR): ").strip().upper()
            amount = input("Enter Amount (NZD): ").strip()
            
            if account_no.isdigit() and amount:
                try:
                    make_transaction(int(account_no), currency_code, float(amount))
                except ValueError:
                    print("❌ Invalid amount")
            else:
                print("❌ Invalid input")
                
        elif choice == '2':
            print("\n📋 All Transactions:")
            transactions = view_transactions()
            if transactions:
                print(f"\n{'Trans ID':<10} {'Account':<10} {'Currency':<10} {'Amount (NZD)':<15} {'Date':<20}")
                print("-" * 70)
                for trans in transactions:
                    print(f"{trans[0]:<10} {trans[1]:<10} {trans[2]:<10} ${trans[3]:<14.2f} {trans[4]:<20}")
            else:
                print("No transactions found.")
                
        elif choice == '3':
            account_no = input("\nEnter Account Number: ").strip()
            if account_no.isdigit():
                transactions = view_transactions(int(account_no))
                if transactions:
                    print(f"\n📋 Transactions for Account {account_no}:")
                    print(f"\n{'Trans ID':<10} {'Currency':<10} {'Amount (NZD)':<15} {'Converted':<15} {'Date':<20}")
                    print("-" * 75)
                    for trans in transactions:
                        converted = trans[3] * trans[6]
                        print(f"{trans[0]:<10} {trans[2]:<10} ${trans[3]:<14.2f} {trans[5]}{converted:<14.2f} {trans[4]:<20}")
                else:
                    print(f"No transactions found for Account {account_no}")
            else:
                print("❌ Invalid Account Number")
                
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice. Please try again.")

def view_info_menu():
    """
    View information submenu
    
    Provides read-only views of:
    - All banks in the system
    - All available currencies and exchange rates
    - All customers
    - All accounts
    - Return to main menu
    """
    while True:
        print_header("📊 VIEW INFORMATION")
        print("  1. View All Banks")
        print("  2. View All Currencies")
        print("  3. View All Customers")
        print("  4. View All Accounts")
        print("  5. Back to Main Menu")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            print("\n🏦 All Banks:")
            banks = view_banks()
            if banks:
                print(f"\n{'ID':<5} {'Bank Name':<25} {'SWIFT Code':<15} {'Branch':<12} {'Country':<15}")
                print("-" * 75)
                for bank in banks:
                    print(f"{bank[0]:<5} {bank[1]:<25} {bank[2]:<15} {bank[3]:<12} {bank[4]:<15}")
            else:
                print("No banks found.")
                
        elif choice == '2':
            print("\n💱 All Currencies:")
            currencies = view_currencies()
            if currencies:
                print(f"\n{'Code':<8} {'Name':<25} {'Symbol':<8} {'Rate':<12} {'Active':<8}")
                print("-" * 65)
                for curr in currencies:
                    active = "Yes" if curr[4] == 1 else "No"
                    print(f"{curr[0]:<8} {curr[1]:<25} {curr[2]:<8} {curr[3]:<12.4f} {active:<8}")
            else:
                print("No currencies found.")
                
        elif choice == '3':
            print("\n👤 All Customers:")
            customers = view_customers()
            if customers:
                print(f"\n{'ID':<5} {'Name':<25} {'Email':<30} {'Phone':<15}")
                print("-" * 80)
                for c in customers:
                    print(f"{c[0]:<5} {c[1]:<25} {c[2]:<30} {c[3]:<15}")
            else:
                print("No customers found.")
                
        elif choice == '4':
            print("\n🏦 All Accounts:")
            accounts = view_accounts()
            if accounts:
                print(f"\n{'Account No':<12} {'Type':<15} {'Balance':<12} {'Bank':<20}")
                print("-" * 65)
                for acc in accounts:
                    print(f"{acc[0]:<12} {acc[1]:<15} ${acc[2]:<11.2f} {acc[3]:<20}")
            else:
                print("No accounts found.")
                
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice. Please try again.")

def main():
    """
    Main program entry point
    
    This function:
    1. Initializes the database (creates tables if they don't exist)
    2. Loads sample data (banks, currencies, customers, accounts)
    3. Displays the main menu and handles user navigation
    4. Runs in a loop until user chooses to exit
    
    The program uses a menu-driven interface where users navigate
    through different submenus to perform various operations.
    """
    print("\n🚀 Initializing Money Exchange System...")
    create_tables()
    initialize_sample_data()
    
    while True:
        main_menu()
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            customer_menu()
        elif choice == '2':
            account_menu()
        elif choice == '3':
            transaction_menu()
        elif choice == '4':
            view_info_menu()
        elif choice == '5':
            print("\n👋 Thank you for using Money Exchange System!")
            print("💰 Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Made with Bob
