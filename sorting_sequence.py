# Sorting Sequence

t = 10,3,4,8,9,2,6,1

print(t)
print(sorted(t))


t = 1 + 1j, 10, 20
try:
    print(sorted(t))
except Exception as e:
    print(e)

d = {3:100, 2:200, 3:300, 2:400}
print(sorted(d))


d = {'b':100, 'a':50, 'c': 10}
print(sorted(d))

print(sorted(d, key=lambda k: d[k]))

t = "this", "parrot", "is", "a", "late", "bird"

print(sorted(t))

def sort_key(s):
    return len(s)

print(sorted(t, key=sort_key))

print(sorted(t, key=lambda s: len(s)))

t = 'a'*4, 'b'*4, 'c'*4,'d'*4


t = "this", "parrot", "is", "a", "late", "bird"
print(t)


res = list(t).sort(key=lambda s:len(s))
print(t)

from timeit import timeit
import random
random.seed(0)

n = 10_000_000
l = [random.randint(0,100) for n in range(n)]

print(timeit(stmt='sorted(l)', globals=globals(), number=1))

print(timeit(stmt='l.sort()', globals=globals(), number = 1))
