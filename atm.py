def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# User accounts database
users = {
    "priya": {"password": "123", "account": {"balance": 1000, "transactions": []}},
    "siri": {"password": "hello", "account": {"balance": 2000, "transactions": []}}
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Authenticate user
    if username in users and users[username]['password'] == password:
        account = users[username]['account']
        print(f"Welcome, {username}!")

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '5':
                print("Exiting ATM...")
                break

            if choice in choices:
                if choice == '1' or choice == '2':
                    amount = float(input("Enter amount: "))
                    choices[choice](account, amount)
                else:
                    print(choices[choice](account))
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Access denied.")

    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Thank you for using the ATM. Goodbye!")
        break