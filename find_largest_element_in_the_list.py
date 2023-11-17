# Finding largest element in the list

## Approach one

list1 = [10, 20, 4, 45, 99]
print(id(list1), list1)

list1.sort()


print(list1[-1])


## Approach two

def find_max(lst):
    if isinstance(lst, (list, tuple)):
        max_num = lst[0]

        for i in lst[1:]:
            if i > max_num:
                max_num = i
        return max_num
    else:
        raise ValueError("argument is not an iterable")


list1 = [-10, -20, -200, -4, -45, -99]

res = find_max(list1)
print(res)


res = find_max(10)
print(res)

