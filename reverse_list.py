"""

Reversing a List in Python
Below are the approaches that we will cover in this article:

Using the slicing technique
Reversing list by swapping present and last numbers at a time
Using the reversed() and reverse() built-in function
Using a two-pointer approach
Using the insert() function
Using list comprehension
Reversing a list using Numpy

"""

## Using slicing technique

ls = [x for x in range(5)]
print(ls, id(ls))
rev_list = ls[::-1]
print(rev_list, id(rev_list))


## Using In built reverse and reversed method

ls = [x for x in range(5)]

ls.reverse()
print(ls)
print(list(reversed(ls)))


## Reverse a list using a two-pointer approach

ls = [x for x in range(1,15,2)]

def rev_a_list(lst):
    left = 0
    right = len(lst) - 1

    while (left < right):
        temp = lst[left]

        lst[left] = lst[right]
        lst[right] = temp

        left += 1
        right -= 1
    return lst
print("Initial List : ", ls)
print("Reveresed list : ", rev_a_list(ls))


ls = [x for x in range(1,15,2)]
def rev(lst):
    new_lst = []
    for element in lst:
        new_lst.insert(0, element)
    return new_lst

res = rev(ls)
print(res)



ls = [x for x in range(1,15,2)]
start = len(ls) - 1

new_lst = [ls[i] for i in range(start, -1, -1)]
print(ls, "reversed to ->", new_lst)
    
