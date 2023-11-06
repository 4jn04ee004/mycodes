from dis import dis

dis(compile('(1,2,3,"a")', 'string', 'eval'))

dis(compile('[1,2,3,"a"]', 'string', 'eval'))

from timeit import timeit

print(timeit("(1,2,3,4,5,6,7,8,9)", number = 10_00_000))
print(timeit("[1,2,3,4,5,6,7,8,9]", number = 10_00_000))

import sys
t = tuple()
prev = sys.getsizeof(t)
for i in range(100):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items : {size_c}, delta={delta}')

print()

l = list()
prev = sys.getsizeof(l)
for i in range(100):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items : {size_c}, delta={delta}')
    

print()

l = list()
prev = sys.getsizeof(l)
for i in range(100):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items : {size_c}, delta={delta}')
    
