class MagicalPrime:
    def __init__(self, number):
        self.number = number
    
    def is_prime(self):
        if self.number <= 1:
            return False
        if self.number <= 3:
            return True
        if self.number % 2 == 0 or self.number % 3 == 0:
            return False
        i = 5
        while i * i <= self.number:
            if self.number % i == 0 or self.number % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def is_magical(self):
        
        return self.is_prime() and self.sum_of_digits_prime()
    
    def sum_of_digits_prime(self):
        digit_sum = sum(int(digit) for digit in str(self.number))
        return MagicalPrime(digit_sum).is_prime()


number = 37
magical_prime = MagicalPrime(number)
if magical_prime.is_magical():
    print(f"{number} is a magical prime number!")
else:
    print(f"{number} is not a magical prime number.")
