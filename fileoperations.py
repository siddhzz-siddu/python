fileptr=open("gfd.txt","r")
if fileptr:
    print("opened successfull")
fileptr=open("sf.txt","a")
fileptr.write("welcome to bitm")
print(fileptr)
if fileptr:
    print("opened successfully")
fileptr.close()