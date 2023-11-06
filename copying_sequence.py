## Copying sequences

l1 = [1, 2, 3]

l1_copy = []

for item in l1:
    l1_copy.append(item)

print(l1_copy)
print(id(l1), id(l1_copy))

l3 = [1,2,3]

for i in range(len(l1)):
    print(id(l1[i]), id(l1_copy[i]), id(l3[i]))

class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f'Line({self.p1},{self.p2})'
    
