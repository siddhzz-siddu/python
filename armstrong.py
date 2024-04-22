def is_armstrong_number(num):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    
    armstrong_sum = 0
    
    
    for digit_char in num_str:
        digit = int(digit_char)
        armstrong_sum += digit ** num_digits
    
    
    return armstrong_sum == num


number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")