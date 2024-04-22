class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}\nBalance: ${self.balance}")

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value
        except ValueError:
            print("Please enter a valid numerical value.")

account_number = input("Enter your account number: ")
initial_balance = get_valid_input("Enter initial balance: $")

account = BankAccount(account_number, initial_balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = get_valid_input("Enter deposit amount: $")
        account.deposit(amount)
    elif choice == '2':
        amount = get_valid_input("Enter withdrawal amount: $")
        account.withdraw(amount)
    elif choice == '3':
        account.display_balance()
    elif choice == '4':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
