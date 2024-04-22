class MagicalPrime:
    def __init__(self, number):
        self.number = number
    
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def reverse_number(self, num):
        return int(str(num)[::-1])
    
    def is_magical_prime(self):
        if not self.is_prime(self.number):
            return False
        reversed_num = self.reverse_number(self.number)
        return self.is_prime(reversed_num)

number = int(input("Enter a number: "))
magical_prime = MagicalPrime(number)
if magical_prime.is_magical_prime():
    print(f"{number} is a magical prime number!")
else:
    print(f"{number} is not a magical prime number.")
    
class NeonNumber(MagicalPrime):
    def __init__(self, number):
        self.number = number
    
    def is_neon(self):
        square = self.number * self.number
        digit_sum = sum(int(digit) for digit in str(square))
        return digit_sum == self.number


number = int(input("Enter a number: "))
neon_number = NeonNumber(number)
if neon_number.is_neon():
    print(f"{number} is a neon number!")
else:
    print(f"{number} is not a neon number.")
    
class NameXPattern(MagicalPrime):
    def __init__(self, name):
        self.name = name
    
    def display_x_pattern(self):
        length = len(self.name)
        for i in range(length):
            for j in range(length):
                if i == j or j == length - i - 1:
                    print(self.name[j], end='')
                else:
                    print(' ', end='')
            print()

name = input("Enter your name: ")
name_x_pattern = NameXPattern(name)
name_x_pattern.display_x_pattern()

class StringReverser:
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        return self.string[::-1]


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse()
    print("Reversed string:", reversed_string)

    
    
class BankAccount(NameXPattern,NeonNumber):
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


