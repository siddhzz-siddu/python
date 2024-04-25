#It returns the address of variables, classes, list,set,
#tuples,dict and object,etc
'''
# id of 5
print("id of 5 =", id(5))

a = 5

# id of a
print("id of a =", id(a))

b = a

# id of b
print("id of b =", id(b))

c = 5.0

# id of c
print("id of c =", id(c))


apple=20
banana=20
print("id of apple =", id(apple))
print("id of banana =", id(banana))


print(apple is banana)
print(apple == banana)
'''

pineapple=[10,20,30]
grapes=[10,20,30]
print("id of pineapple =", id(pineapple))
print("id of grapes =", id(grapes))

print(pineapple is grapes)
print(pineapple == grapes)