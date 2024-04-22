psd=1234
password=int(input("enter password"))
for i in range(0,3):
    if psd!=password:
        print('wrong psd')
        password=int(input("enter password"))
    else:
        print('correct')
    