a=(1,2,3,4,5)
b=(6,7,8,9)
print(a)
print(type(a))
print(a*2)
print(max(a))
print(min(a))
print(len(a))
print(a[1])
c=a+b
print(c)
for i in a:
    if i in b:
        b.append(i)
    print(b)
print(b)