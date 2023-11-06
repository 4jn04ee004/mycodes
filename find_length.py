## Finding length of the list

test_list = [1, 4, 5, 7, 8]

count = 0

for x in test_list:
    count+=1
print("Length of the given list : ", count)


## Find the Length of a List  Using Enemerate

for i, j in enumerate(test_list):
    x,y = i,j

## Find the Length of a List in Python using sum()

total = sum([1 for num in test_list])
print(total)

ls = [x for x in range(100)]

count = sum(1 for num in ls)
print(count)



## Find the Length of a List in Python using recursion

def count(List):
    if not List:
        return 0
    else:
        print(List)
        return 1 + count(List[1:])


# Test the function with a sample list
List = [x for x in range(10)]
print("The length of the list is:", count(List))

## Find the Length of a List in Python using Collections

from collections import Counter
test_list = [1,4,5,8,9,2]

res = Counter(test_list).values()
print(sum(res))
