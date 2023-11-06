# Python3 code to demonstrate 
# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))


new = [sub.replace("G", "e") if sub[0] == "G" else sub for sub in test_list  ]
print("The new list is : " + str(new))


lst = ["apple", "oranges", "banana"]

new = [x[0].upper() + x[1::] for x in lst]


print(new)




