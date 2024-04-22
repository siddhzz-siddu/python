class Mango:
    def __init__(self):
        print("this is what?")
    def priya(self):
        print("this is without para")
    def siri(self,a,b):
        print(a+b,"this is with para")
    def magicalprime(self,a):
        print("check it magical prime or not")
    def neon(self,a):
        square = a ** 2
        sum_of_digits = sum(int(digit) for digit in str(square))
        if sum_of_digits == a:
            print(f"{a} is a neon number.")
        else:
            print(f"{a} is not a neon number.")
man=Mango()
man.priya()
man.siri(10,20.5)
man.magicalprime(101)
man.neon(7)
man.neon(9)


'''
0 is neon
1 is neon
2^2==2
3^2==3
4^2==4(16=1+6=7==4)
5^2==5(25=2+5=7==5)
6^2==6(36=3+6=9==6)              magical prime=71 is prime its reverse is 17 it is also prime
7^2==7(49=4+9=13=1+3=4==7)
8^2==8(64=6+4=10=1+0=1==8)
9^2==9(81=8+1=9==9)
'''