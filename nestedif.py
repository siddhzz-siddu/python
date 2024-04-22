email="priya"
password=1234
otp=4567
uemail=str(input("enter email"))
upass=int(input("enter password"))
if(email==uemail):
    if(password==upass):
        print("login sucess")
        uotp=int(input("enter otp"))
        if(otp==uotp):
            print("transaction successfull")
        else:
            print("transaction failed")
    else:
        print("login  failed due to password")
else
:
    print("password failed due to email")
