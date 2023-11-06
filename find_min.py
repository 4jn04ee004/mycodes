## Minimum of two numbers

def minimum(a: int, b: int):
    return a if a < b else b

res = minimum(10,20)
print(res)

## Using lambda function
func = lambda a,b : a if a < b else b

res = func(21, 31)
print(res)




## finding minimum in collaboration with isinstance

def find_min(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a if a < b else b
    else:
        r
    
res = find_min(66.5, 66)
print(res)


## Approach : Sorts the given two numbers in ascending order and
## returns the first element, which is the minimum of the two.

class InvalidNumberEntered(Exception):
    "Raise this exception if entered number is other than integer or float"
    pass

def find_min(a,b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return sorted([a,b])[0]
        else:
            raise InvalidNumberEntered
    except InvalidNumberEntered:
        print("Please enter either an integer or float value")

res = find_min(26,37)
print(res)
find_min("abc", 17)
    

res = find_min(22,11)
print(res)

## APPROACH:
## This program finds the minimum of two numbers using the reduce function of functools module.

from functools import reduce

min_find = lambda x, y: x if x < y else y

lst = [x+5 for x in range(10, 1,-2)]
print(lst)

min_num = reduce(min_find, lst)
print("Printing list : ", lst)
print("Minimum value in the list is : ", min_num)

func = lambda x,y : x + y

res = reduce(func, lst)
print("sum of the element in the list : ", res)
