## Different ways to clear a list in Python

ls = [i for i in range(10)]

print(ls)
print()

## Will not pop up all the elements
for i in ls:
    print(i)
    ls.pop()
    print(len(ls))

print(ls)

ls = [i for i in range(10)]

for i in ls[:]:
    print(i)
    ls.pop()
    print(len(ls))

print(ls)


## Another approach

print("**" * 50)
ls = [i for i in range(10)]

i = len(ls)
while len(ls) != 0:
    ls.pop(-i)
    i = len(ls)

print("List :: ", ls)


## Another approach using "pop"
ls = [i for i in range(10)]

print("List before deletion:", ls)
while len(ls) !=0:
    ls.pop()

print("List after deletion :", ls)
    


## Another approach using "remove"
ls = [i for i in range(10)]

new_ls = ls[:]

print("List before deletion:", ls)
for i in new_ls:
    ls.remove(i)

print("List after deletion :", ls)




