try:
    num=int(input("enter num"))
    assert num%2==0
except:
    print("not an even")
else:
    reciprocal=1/num
    print(reciprocal)