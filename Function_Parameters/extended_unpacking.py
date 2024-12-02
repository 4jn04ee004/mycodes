# Dict unpacking

d1 = {"a" : 10, "b" : 20}
d2 = {"apple": "red", "banana": "yellow"}

d3 = {**d1, **d2}
print(d3)

import json
j = json.dumps(d3)
print(j)

l = [1,2,3,4,5,6]
a = l[0]
b = l[1:]
print(a)
print(b)

a, *b = l
print(a)
print(b)

# Set doesn't have ordering
try:
    s = {1, 2, 3}
    a = s[0]
    b = s[1:]
except TypeError as e:
    print(e)

# Unpacking on string
s = 'python'
a, *b = s
print(a)
print(b)

# Unpacking tuple

t = ('a', 'b', 'c')
a, *b = t
print(a)
print(b)

# Enhanced unpacking
a, b, *c = 'python'
print(a)
print(b)
print(c)

s = 'python'
a,b,c,d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

s1 = 'abc'
s2 = 'def'
s3 = [*s1, *s2]
print(s3)

# concatenation of sets
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8, 9}

try:
    s = s1 + s2
except TypeError as err:
    print(err)

# Unpacking of sets
s = {*s1, *s2}
print(s)

# Union on sets

s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
s3 = {10, 11, 12, 13}

s = s1.union(s2).union(s3)
print(s)

s = s1.union(s2, s3)
print(s)

s = {*s1, *s2, *s3}
print(s)

s = [*s1, *s2, *s3]
print(s)


d1 = {"macro" : "4g", "mmwave": "5g", "sub6": "5g"}
d2 = {"helm" : "bundle", "robin": "bundle"}
d = {*d1, *d2}
print(d)

