# Database Design Project: Finance Money Exchange Application

## 1. Project Overview
This project presents the Entity-Relationship (ER) design for a financial software application specializing in currency exchange. The database is architected to manage core banking structures, customer accounts, multi-currency support, and precise transaction logging.

## 2. Entities and Attributes
The system consists of five primary entities, each containing at least five attributes to ensure comprehensive data coverage and relational integrity:

### **BANK**
*Stores information regarding participating financial institutions.*
*   **Bank_ID (PK)**: Unique identifier for the bank.
*   **Bank_Name**: Official name of the bank.
*   **Swift_Code**: International standardized bank code.
*   **Branch_Code**: Specific branch identification.
*   **Country**: The country where the bank is registered.

### **CUSTOMER**
*Contains identity and contact details for users of the exchange service.*
*   **Customer_ID (PK)**: Unique identifier for the customer.
*   **Full_Name**: Legal name of the user.
*   **Email**: Primary contact email address.
*   **Phone**: Contact telephone number.
*   **Passport_No**: Identification number for KYC (Know Your Customer) compliance.

### **ACCOUNT**
*Represents the financial accounts held by customers within specific banks.*
*   **Account_No (PK)**: Unique account number.
*   **Bank_ID (FK)**: Reference to the managing bank.
*   **Customer_ID (FK)**: Reference to the account owner.
*   **Account_Type**: Category of account (e.g., Savings, Checking).
*   **Balance**: Current available funds.

### **TRANSACTION**
*Records the details of every currency exchange executed.*
*   **Trans_ID (PK)**: Unique transaction reference number.
*   **Account_No (FK)**: The account from which funds are drawn.
*   **Currency_Code (FK)**: The target currency involved in the exchange.
*   **Amount**: The value of the transaction.
*   **Trans_Date**: Timestamp of the exchange execution.

### **CURRENCY**
*Defines the supported currencies and their respective exchange metrics.*
*   **Currency_Code (PK)**: ISO standard currency code (e.g., USD, NZD).
*   **Name**: Full name of the currency.
*   **Symbol**: Visual representation (e.g., $, €).
*   **Rate**: The current exchange rate relative to the base currency.
*   **Active**: Boolean status indicating if the currency is available for trade.

## 3. Relationship Specifications
The database utilizes **One-to-Many (1:N)** relationships to ensure logical data flow and referential integrity:

1.  **BANK to ACCOUNT (1:N)**: One bank can manage multiple customer accounts.
2.  **CUSTOMER to ACCOUNT (1:N)**: One customer can hold multiple accounts across different banks or currencies.
3.  **ACCOUNT to TRANSACTION (1:N)**: A single account can initiate numerous transaction records.
4.  **CURRENCY to TRANSACTION (1:N)**: A specific currency can be involved in multiple transaction events.
5.  **CUSTOMER to TRANSACTION (1:N)**: A customer may generate a history of multiple exchange transactions.

## 4. Implementation Notes
The ER diagram for this project follows **Chen's Notation** standards:
*   **Rectangles**: Represent Entities.
*   **Ovals**: Represent Attributes (Primary Keys are underlined).
*   **Diamonds**: Represent Relationships.