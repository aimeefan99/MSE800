# Database Design Project: Finance Money Exchange Application (V2)

## 1. Project Overview
This database design supports a professional currency exchange application. A key feature of this model is the support for **Joint Accounts**, allowing a Many-to-Many (M:N) relationship between customers and accounts.

## 2. Entities and Attributes

### **CUSTOMER**
*   **Customer_ID (PK)**: Unique identifier for the customer.
*   **Full_Name**: Legal name.
*   **Email / Phone**: Contact details.
*   **Passport_No**: Required for KYC compliance.

### **ACCOUNT**
*   **Account_No (PK)**: Unique account identifier.
*   **Bank_ID (FK)**: Associated banking institution.
*   **Account_Type**: Savings, Checking, or Joint.
*   **Balance**: Current funds available.
*   **Date_Opened**: Account creation timestamp.

### **BANK / TRANSACTION / CURRENCY**
*(Standard financial attributes as defined in the previous version, including PKs and relevant FKs for transaction tracking.)*

## 3. Relationship Specifications

### **CUSTOMER to ACCOUNT (M:N)**
Unlike standard personal banking, this system supports **Joint Accounts**:
*   **Many Customers to One Account**: Multiple family members or business partners can own a single account.
*   **One Customer to Many Accounts**: An individual can hold multiple accounts (e.g., USD account, NZD account).
*   **Implementation**: This is managed via the `ACCOUNT_HOLDER` associative table containing `Customer_ID (FK)` and `Account_No (FK)`.

### **Other Relationships**
*   **BANK to ACCOUNT (1:N)**: One bank manages multiple accounts.
*   **ACCOUNT to TRANSACTION (1:N)**: Each transaction is tied to a specific funding account.
*   **CURRENCY to TRANSACTION (1:N)**: Each exchange involves a specific target currency.

## 4. Design Justification
By utilizing an **M:N relationship** for accounts, the system gains the flexibility required for modern financial services, such as shared corporate folders and multi-user household management, ensuring the database remains scalable and compliant with complex banking regulations.