## Sum of digit in numbers in the list

# Approach one using map function

lst = [18, 16, 10, 28, 20, 10, 38, 58]

func = lambda element: sum(int(sub) for sub in str(element))

resp = list(map(func, lst))
print(resp)


## using function

from functools import reduce

def sum_of_digit(lst):
    new_list = [[int(y) for y in str(x)] for x in lst]
    print(new_list)

    func = lambda args : sum(*args)

    res = list(map(func, new_list))
    return res

print(sum_of_digit(lst))

    
