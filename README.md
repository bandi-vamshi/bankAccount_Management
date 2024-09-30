### Bank Account Simulation in Python
## Project Overview

This Python project simulates basic banking operations such as account creation, checking balance, depositing money, and withdrawing money. It provides a simple interface for users to interact with their bank accounts, allowing them to perform essential tasks like deposits, withdrawals, and balance inquiries.

This project is designed to help understand the use of functions, conditionals, loops, and working with variables and data structures in Python.

## Features

Create a New Bank Account: Captures the account holder’s name, account number, mobile number, and initial balance.
Deposit Money: Allows users to add money to their account balance.
Withdraw Money: Enables users to withdraw money, with a condition to prevent overdraws.
Check Balance: Displays the current balance of the account.
Close Account: Deletes the account from the system.
Basic Input Validation: Ensures that account numbers are unique and balances cannot go below zero.
Usage

# Creating an Account:
The user is prompted to enter details like name, account number, mobile number, and an initial deposit.
The account is stored and can be accessed for further transactions.

# Depositing Money:
The user inputs the account number and the amount to deposit.
The account balance is updated with the new amount.

# Withdrawing Money:
The user enters the account number and the amount to withdraw.
The system checks for sufficient balance before processing the withdrawal.

# Checking Balance:
The user enters the account number, and the system displays the current balance for that account.

# Closing an Account:
The user can close an account by entering the correct account number, which removes it from the system.

# How to Run the Project
Clone the repository or download the Python script.
Run the script using Python 3.x.
Follow the on-screen prompts to perform the different operations.

# python bank_account_simulation.py

# Example output:
1. Create Account 
2. Deposit 
3. Withdraw 
4. Balance Enquiry 
5. Close Account 
6. Exit
Enter your choice:

## Future Improvements
Implement error handling for invalid inputs (e.g., non-numeric account numbers or negative deposit amounts).
Introduce password-based authentication for better security.
Add file-based data storage to persist account information between sessions.

## License
This project is open-source and available under the MIT License.
