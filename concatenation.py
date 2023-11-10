## Concatenation

l1 = [1,2,3]
l2 = ['a', 'b', 'c']

print(id(l1), id(l2))

l1 = l1 + l2
print(l1, id(l1))


## In Place concatenation, memory address of the mutable sequence will not change


l = [1,2,3]
print(l, id(l))
l += ['a', 'b']
print(l, id(l))
