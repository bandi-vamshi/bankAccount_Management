
accounts = {}
def create_Account():
    value = input("Create an Account (yes/no): ")
    if value.lower() == 'yes':
        name = input("Enter your Name: ")
        acc_number = int(input("Enter your account Number: "))
        mbl_num = int(input("Enter your mobile Number: "))
        initial_blc = float(input("Enter the minimum Balance: "))

        if acc_number in accounts:
            print(f"Account with number {acc_number} already exists.")
        else:
            accounts[acc_number] = {
                'name': name,
                'mobile_num': mbl_num,
                'Balance': initial_blc
            }
            print('Account created successfully.')
        print("*" * 50)
    else:
        print("Thank you for visiting the Bank.")

def deposit():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        amount = float(input("Enter the amount: "))
        accounts[acc_num]['Balance'] += amount
        print(f'{round(amount, 2)} credited to your Bank account.')
    else:
        print("Account not exists, create an account.")
        create_Account()

def withdraw():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        amount = float(input("Enter the amount: "))
        if accounts[acc_num]['Balance'] >= amount:
            accounts[acc_num]['Balance'] -= amount
            print(f'{round(amount, 2)} debited from your account.')
        else:
            print("Insufficient balance.")
    else:
        print("Account does not exist, please create an account.")
        create_Account()

def blc_checking():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        print(f"Your Bank balance is {accounts[acc_num]['Balance']}.")
    else:
        print("Account does not exist, please create an account.")
        create_Account()

def close_account():
    acc_num = int(input("Enter your account number: "))
    if acc_num in accounts:
        accounts.pop(acc_num)
        print("Your account has been closed.")
    else:
        print("Account does not exist, please create an account.")

def main():
    while True:
        print('\n1. Create Account \n2. Deposit \n3. Withdraw \n4. Balance Enquiry \n5. Close Account \n6. Exit')
        option = int(input("Enter your choice: "))
        match option:
            case 1:
                create_Account()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                blc_checking()
            case 5:
                close_account()
            case 6:
                print("Exiting program.")
                break
            case _:
                print("Invalid option, try again.")
        print('*' * 50)

if __name__ == '__main__':
    main()
