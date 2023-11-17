## Python program to find smallest number in a list

lst = [16, 20, 10, 30]

## Approach one
print(sorted(lst, reverse=False)[0])

## Approach two

def sort(lst):
    num = len(lst)
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
        
    return smallest

res = sort(lst)
print(res)

## using min method

print(min(lst))

lst = ['1abc', 'abb', 'abbcc', 'abbccdd']

#print(min(lst, key= lambda val: x for x in [char in char in val] if isinstance(int(x), int)))

## Using 
## Using reduce and lambda function
