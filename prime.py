a=[]
n=int(input('enter size'))
for i in range(0,n):
    ele=int(input("enter elements"))
    a.append(ele)
for i in range(0,n):
    if a[i]%4==0 and a[i]>1000:
        print(a[i],"is a leap year")
    else:
        print(a[i],"is not a leap year")

if n > 1:
    for num in a:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
else:
    print(n, "is not a prime number")