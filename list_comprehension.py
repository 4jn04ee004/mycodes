## List comprehension


squares = []

for i in range(1,101):
    squares.append(i ** 2)

# print(squares)

sq = [x ** 2 for x in range(1,101)]

# print(sq)

print(sq[0:10])

sq = [x ** 2 for x in range(1,101) if x % 2 == 0]
print(sq)

sq = [
    x ** 2
    for x in range(1,101)
    if x % 2 != 0
    ]

print(sq)


compiled_code = compile('[i**2 for i in (1,2,3)]',
                        filename = 'string', mode='eval')

print(compiled_code)

import dis

dis.dis(compiled_code)


table = [
    [i * j for i in range(1,11)]
    for j in range(1,11)
    ]
print(table)


l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

result = [
    i + j for i in l1
    for j in l2
    ]



print(result)

result = [
    i + j for j in l1
    for i in l2
    ]


l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']

res = [s1 + s2 for s1 in l1 for s2 in l2 if s1 != s2]
print(res)





l1 = [1,2,3,4,5,6,7,8,9]
l2 = ['a', 'b', 'c', 'd']

x = list(zip(l1, l2))
print(x)

print(list(enumerate(l1)))

print(list(enumerate(l2)))

res = []

for index_1, item_1 in enumerate(l1):
    for index_2, item_2 in enumerate(l2):
        if index_1 == index_2:
            res.append((item_1, item_2))

print("Using for loop", res)

## Using list comprehension

res = [(item_1, item_2) for index_1, item_1 in enumerate(l1)
       for index_2, item_2 in enumerate(l2)
       if index_1 == index_2]

print("Using list comprehension", res)


l = [1,2,3]
x = sum(l)
print(x)

v1 = (1,2,3,4,5,6)
v2 = (10,20,30,40,50,60)

dot = 0

for i in range(len(v1)):
    dot += (v1[i] * v2[i])

print(dot)

res = zip(v1, v2)

if isinstance(res, type):
    print(list(res))
print(list(res))


for i, j in zip(v1,v2):
    print(i,j)


from datetime import datetime

print(datetime.now())

def log(msg, current_dt=datetime.now()):
    print(msg, current_dt)
    







