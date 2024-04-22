'''
try:
    #code that may cause exception
except:
     #code to run when exception occurs
'''


try:
    num=10
    den=0
    result=num/den
    print(result)
except:
    print("error:denominator cannot be 0")