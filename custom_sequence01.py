## Assigment in mutable sequence

marker = '*' * 10

l = [1,2,3,4,5]
print(id(l))

print(l[0:3])
print(marker)
l[0:3] = 'python'

print(id(l), l)

print(marker)

l = [1,2,3,4,5]
print(id(l))
l[2:5] = []
print(id(l), l)


print(marker)
