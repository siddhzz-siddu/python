'''
1) Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010

2) Write a Python program that accepts a string and calculates the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2

3) Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
                           
4)Write a Python program to print the alphabet pattern 'E'.
Expected Output:

5)Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days


    
'''    
#--------------------------------


# Create an empty list named 'items'
items = []

# Take user input and split it into a list of strings using ',' as the delimiter
num = [x for x in input().split(',')]

# Iterate through each element 'p' in the 'num' list
for p in num:
    # Convert the binary string 'p' to its decimal equivalent 'x'
    x = int(p,2)
    
    # Check if 'x' is divisible by 5 (i.e., when divided by 5 there's no remainder)
    if not x % 5:
        # If 'x' is divisible by 5, add the binary string 'p' to the 'items' list
        items.append(p)

# Join the elements in the 'items' list separated by ',' and print the result
print(','.join(items))



#-----------------------------
'''
# Prompt the user to input a string and store it in the variable 's'
s = input("Input a string")

# Initialize variables 'd' (for counting digits) and 'l' (for counting letters) with values 0
d = l = 0

# Iterate through each character 'c' in the input string 's'
for c in s:
    # Check if the current character 'c' is a digit
    if c.isdigit():
        # If 'c' is a digit, increment the count of digits ('d')
        d = d + 1
    # Check if the current character 'c' is an alphabet letter
    elif c.isalpha():
        # If 'c' is an alphabet letter, increment the count of letters ('l')
        l = l + 1
    else:
        # If 'c' is neither a digit nor an alphabet letter, do nothing ('pass')
        pass

# Print the total count of letters ('l') and digits ('d') in the input string 's'
print("Letters", l)
print("Digits", d)
'''

#----------------------------

# Import the 're' module for regular expressions
import re

# Prompt the user to input a password and store it in the variable 'p'
p = input("Input your password")

# Set 'x' to True to enter the while loop
x = True

# Start a while loop that continues until 'x' is True
while x:  
    # Check conditions for a valid password:
    # Password length should be between 6 and 12 characters
    if (len(p) < 6 or len(p) > 12):
        break
    # Password should contain at least one lowercase letter
    elif not re.search("[a-z]", p):
        break
    # Password should contain at least one digit
    elif not re.search("[0-9]", p):
        break
    # Password should contain at least one uppercase letter
    elif not re.search("[A-Z]", p):
        break
    # Password should contain at least one special character among '$', '#', '@'
    elif not re.search("[$#@]", p):
        break
    # Password should not contain any whitespace character
    elif re.search("\s", p):
        break
    else:
        # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
        print("Valid Password")
        x = False
        break

# If 'x' remains True, print "Not a Valid Password"
if x:
    print("Not a Valid Password")


#---------------------------
'''   
# Initialize an empty string named 'result_str'
result_str = ""

# Iterate through rows from 0 to 6 using the range function
for row in range(0, 7):
    # Iterate through columns from 0 to 6 using the range function
    for column in range(0, 7):
        # Check conditions to determine whether to place '*' or ' ' in the result string
        
        # If conditions are met, place '*' in specific positions based on row and column values
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
            result_str = result_str + "*"  # Append '*' to the 'result_str'
        else:
            result_str = result_str + " "  # Append space (' ') to the 'result_str'

    result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'

# Print the final 'result_str' containing the pattern
print(result_str)


#--------------------------

# Display a list of months to the user
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

# Request input from the user to enter the name of a month and assign it to the variable 'month_name'
month_name = input("Input the name of Month: ")

# Check the input 'month_name' and provide the number of days based on the entered month
if month_name == "February":
    print("No. of days: 28/29 days")  # Display the number of days in February (28 or 29 days for leap years)
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")  # Display the number of days for months having 30 days
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")  # Display the number of days for months having 31 days
else:
    print("Wrong month name")  # If the entered month name doesn't match any of the
'''