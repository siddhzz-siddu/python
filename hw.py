Employee = {"Name": "Balaji", "Age": 70, "aadhar":200000,"debitcard":12345,"phoneno":8660235206,"dob":2004,"pincode":123456,"height":5.2,"tax":12.5}         

Employee["Name"] = input("Name: ");        
Employee["Age"] = int(input("Age: "));        
Employee["aadhar"] = int(input("aadhar: "));        
Employee["debitcard"] = int(input("Company: "));
Employee["phoneno"]=int(input("phoneno: "))
Employee["dob"]=int(input("dob: "))
Employee["pincode"]=int(input("pin: "))
Employee["height"] =float(input("height: "));        
Employee["tax"] = float(input("tax: "));        
print(Employee)
for i in Employee:
    print(i)