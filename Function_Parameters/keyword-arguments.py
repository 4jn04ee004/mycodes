def func1(a,b,c):
    print(a,b,c)

# Positional arguments
func1(1,2,3)

#Using keyword arguments
func1(a=10, b=30, c=50)

# Incorrect way of passing argument
def func1(a, b, c, *args, d):
    print(a, b, c, args, d)

try:
    func1(10,20,30,40,50)
except TypeError as e:
    print(e)

# Correct way is to use keyword argument after *args

try:
    func1(10,20,30,40,50,d=60)
except TypeError as e:
    print(e)

