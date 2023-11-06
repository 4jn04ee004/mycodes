# Sequence Type

t = ([1,2], 3,4)
try:
    t[0] = [1,2,3]
except Exception as e:
    print("Something went wrong")
    
t[0][0] = 100
print(t)

print('a' in ['a', 'b', 100])

x = {11, 22, 33, 44, 55, 444, 66}
for i in x:
    print(i)


string = ["a", "b", "c"]

print("^-^".join(string))



s = "gnu's not unix"

print(list(enumerate(s)))

print(s.index("n"))

a = [1, 2, 3]
b = a

print(id(a), id(b))

# Slicing always return a new object

c = a[:]
print(id(a), id(c))

# Reversing a string
s = "reverse"
new = s[::-1]
print(new)

# Caveat

from decimal import Decimal

a = Decimal('10.5')
b = Decimal('10.5')

print(a is b)
print(id(a), id (b))

l = [Decimal('10.5')]
l2 = l * 2

print(id(l2[0]), id(l2[1]))


