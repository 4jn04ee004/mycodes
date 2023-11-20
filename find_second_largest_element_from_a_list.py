# Python program to find second largest number in a list

lst = [2,10,15,7,8]

## first approach

def find_second_largest(lst):

    fmax = lst[0]
    lmam = lst[-1]

    for i in lst[1:]:
        if i > fmax:
            
