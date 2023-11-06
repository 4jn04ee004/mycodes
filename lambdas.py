## world of lambdas

# A lambda function that adds 10 to the input argument 

f = lambda x: x + 10 if isinstance(x, int) else 0

val1 = f(5)
print(val1)

val2 = f(100)
print(val2)

val3 = f("abc")
print(val3)


f = lambda x: x + 10 if isinstance(x, int) else int(x+10) if isinstance(x, float) else 0

val4 = f("abc")
print(val4)

val5 = f(5.5)
print(val5)

## Custom sorting using a lambda function as key parameter

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]

mylist = sorted(points2D, key=lambda x: x[1])
print(mylist)


## Use lambda for map function

x = [a for a in range(0,10,2)]

y = list(map(lambda num: num+1, x))
print(y)


## Use lambda for filter function

x = [a for a in range(0,10,3)]
y = list(filter(lambda x : x%2 == 0, x))
print("Original list : ", x)
print(y)

## Use lambda for reduce function

from functools import reduce
x = [a for a in range(0,10,3)]
y = reduce(lambda a,b : a+b, x)
print(y)

## Use MAP with normal function

def add_one(num):
    return num+1

gen_obj = map(add_one, range(10))

print([x for x in gen_obj])

## Make it real time

ip_list = ["192.168.1.1",
           "192.168.1.2",
           "192.168.1.3",
           "192.168.1.4"
           ]


def mod_ip(ip):
    lst = ip.split('.')
    lst[-2] = str(int(lst[-2]) + 1)
    return ".".join(lst)


new_ip = list(map(mod_ip, ip_list))
print(new_ip)


## Use lambda for filter function

# The filter() function works similar to map() function, except,
# it validates True if a condition is met and validates False otherwise.
# It only returns the items of a sequence that validate to True.


check_boolean = filter(bool, ["Pyrate", "", 20, None, ''])
print(check_boolean)
print(list(check_boolean))

for i in check_boolean:
    print(i)


# Unlike map() and filter(), reduce() function doesn’t return a new sequence. Instead, it returns a single value.
# In Python 3, reduce() has been moved to the functools library

from functools import reduce
log = print
def addition(x, y):
    return x + y

lst = [1, 2, 3, 4]
log(reduce(addition, lst))
