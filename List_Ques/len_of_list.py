lst = ["orch", "catalog", "CI", "naming", "ipam"]

# Method 1

counter = 0
for _ in lst:
    counter += 1

print(f"Length of the list using naive method: {counter}")

# Method 2

print("Length of the list using in-build len function:", len(lst))

# Method 3

count = sum([1 for _ in lst])
print("Length of list using list comprehension:", count)

# Method 4

def recur(lst):
    if not lst:
        return 0
    else:
        return 1 + recur(lst[:-1])

count = recur(lst)
print(count)


# Method 4
count = 0
for i, val in enumerate(lst):
    print(i, val)
    count += 1
print("Total list element count :", count)
