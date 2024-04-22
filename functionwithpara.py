def priya(a,b):
    print(a+b)
    
test_dict={"fname":priya,"age":50,"address":"salem"}
print("the original dictionary is:"+str(test_dict))
res=test_dict['fname'](10,20)