# Ways to define tuple

a = (10, 20, 30)
print(type(a), a)

b = 10, 20, 30
print(type(b), b)

# Not a tuple if single value defined like 

c = (100)
print(type(c), c)

# Defining tuple with single value
d = (100,)
print(type(d), d)


# Unpacking 

a, b, c = 10.5, 11, 22
print(a, b, c)

d, e, f = ["Hello", "My", "World"]
print(d, e, f)

# Iterating through a string
for s in "python":
	print(s)

# Sets 
s = {'p', 'y', 't', 'h', 'o', 'n'}
for i in s:
	print(i)

# List unpacking

lst1 = [10, 20, 30]
lst2 = ["Hello", "World!"]
lst3 = [10.5, "Orch", 1200]

lst4 = [*lst1, *lst2, *lst3]
print(lst4)

lst5 = lst1 + lst2 + lst3
print(lst5)

# Swapping 
# 1st method
a, b = 10, 20
print(a,b)
a, b = b, a
print(a,b)

# 2nd Method
a, b = 10, 20

temp = a
a = b
b = temp
print(a, b)


for e in 'XYZ':
	print(e)

a, b, c = 'XYZ'

print(a, b, c)

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)

# s is an iterable 
for e in s:
    print(e)

# Iterating a dictionary

d = {"a": 1, "b":2, "c":3}
a, b, c = d
print(a, b, c)
