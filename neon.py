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
