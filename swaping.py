# Python Program to Swap Two Elements in a List

def swap(lst, pos1, pos2):
    
    if len(lst) < pos1 or len(lst) < pos2:
        return
        #raise IndexError("bhosdike")
    else:
        print(lst)
        lst[pos1],lst[pos2] = lst[pos2], lst[pos1]
        return lst

l = ["apple", 10, "mango", 20]

print(swap(l, 0,1))

print(l)

# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	# popping both the elements from list
	first_ele = list.pop(pos1) 
	second_ele = list.pop(pos2-1)
	print(first_ele, second_ele)
	
	# inserting in each others positions
	list.insert(pos1, second_ele) 
	list.insert(pos2, first_ele) 
	
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))
