## Count Occurence of an element



## Using dict and for loop
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

d = dict()

for i in lst:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)



## Using in-built count method
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

def countX(lst, n):
    return lst.count(n)

x = 8
y = 100

res = countX(lst, x)

print(f"{x} has occurred {res} times")

res = countX(lst, y)

print(f"{y} has occurred {res} times")

## Count occurrences of an element in a list Using Counter()

from collections import Counter
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
d = Counter(lst)

for value, occurence in d.items():
    print(f"{value} has occurenced {occurence} times in the list")


## Method 5: Count occurrences of an element in a list Using dictionary comprehension

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

d = {item: lst.count(item) for item in lst}
n = 8

print(f"{n} occured {d[n]} times in the list")

## Method: Using list comprehension

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
num = 0

x = [val for val in lst if val == num]
print(len(x))


    

