try:
    even_num=[2,4,6,8]
    print(even_num[5])
except ZeroDivisionError:
    print("denominator cannot be zero")
except IndexError:
    print("index out of bound")