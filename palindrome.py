def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1
    return True

string = input("Enter a string: ")
if is_palindrome(string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")