## Max exmaples

# Naive approach
def maxi(a, b):
    if a > b:
        return a
    else:
        return b

a = 2
b = 4

mx = maxi(a,b)
print(mx)
mx = maxi(b, a)
print(mx)

# Inbuilt function

res = max(a,b)
print(res)

##
a = 10
b = 11
res = a if a>b else b
print(res)

## Using lambda function

func = lambda x,y: x if x > y else y
res = func(a,b)
print(res)


## using list comprehension
max_value = [a if a > b else b]
print(max_value)

