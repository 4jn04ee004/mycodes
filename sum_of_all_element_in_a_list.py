## Sum of number  in List

## First approach

lst = [8, 6, "apple", 10, 8, 20, 10, 8, 8]

sums = 0

for x in lst:
    if isinstance(x, int):
        sums += x
print(sums)


## Another approach

from functools import reduce
lst = [8, 6, "apple", 10, 8, 20, 10, 8, 8]

x = lambda x: x if isinstance(x, int) else 0

new_list = filter(x, lst)

y = lambda x, y : x + y

s = reduce(y, new_list)
print(s)



## Another approach

