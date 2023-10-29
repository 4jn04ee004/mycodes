# Swap first and last element of the list

a = [11, 10, 6, 7, 12]

# approach one

f = a[0]
l = a[len(a)-1]

a[0] = l
a[len(a) - 1] = f

print(a)

# approach two

a = [11, 10, 6, 7, 12]

a[0], a[len(a) -1] = a[len(a)-1], a[0]
print(a)

# approach three

a = [11, 10, 6, 7, 12]

tup = a[len(a)-1], a[0]

a[0], a[len(a)-1] = tup

print(a)

# approach four

a = [110, 10, 6, 7, 120]

first, *middle, last = a

a = [last, *middle, first]

print(a)

