## Assignment in mutable sequences

l = [1,2,3,4,5]
print(id(l))

print(l[0:3])

l[0:3] = 'python'

print(id(l), l)

l[2:5] = ''

print(id(l), l)


l[0:3] = {100, 'x', 'a'}

print(id(l), l)


## Extended Slice

l = [1,2,3,4,5]

print()
print(id(l))

print(l[0:5:2])
l[0:5:2] = 'abc'
print(id(l), l)


l[0:5:2] = [1,3,5]
print(id(l), l)

try:
    l[0:5:2] = ['a', 'b', 'c', 'd']
except ValueError as e:
    print(e)
finally:
    l[0:5:2] = ['a', 'b', 'c']
    print(id(l), l)



