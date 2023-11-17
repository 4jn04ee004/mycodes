## Multiple all numbers in a list

## reduce takes a function and ittrable, reduce applies that function on the
## iterable and produces a cumulative result. Here function takes first two
## elements of the iterable and produces a intermediate result, then function takes
## that intermediate result and third element as an argument and produces a
## cumulative result until the iterable is exhausted.


from functools import reduce
x = [10,20,30,40]

func = lambda x,y : x * y

res = reduce(func, x)
print(res)


def func(x,y):
    print(f"First argument is {x}, and second argument is {y}")
    return x * y

res = reduce(func, x)
print()
print("Final result is : ",res)
