## Custom Sequence 2

from collections import namedtuple

Point = namedtuple('Point', 'x y')

p1 = Point(10.5, 3.2)
print(p1)
x,y = p1
print(x,y)

p1 = Point('abc', [1,2,3])
print(p1)

x,y = p1
print(x,y)


import numbers

print(isinstance(10, numbers.Number))
print(isinstance('abc', numbers.Number))
print(isinstance(10+2j, numbers.Number))
print(isinstance(10.5, numbers.Number))


class Point:

    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x,y)
        else:
            raise TypeError('Point Co-ordinates must be ereal numbers')

    def __repr__(self):
        return f"Point(x={self._pt[0]}, y = {self._pt[1]})"

    def __len__(self):
        return len(self._pt)

    def __getitem__(self, s):
        print("I am called")
        return self._pt[s]

    


p1 = Point(10, 20)
print(p1)

x, y = p1

print(x)
print(y)



class Polygon:

    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
            print(type(self._pts))
        else:
            self._pts = []

    def __repr__(self):
        ptr_str = ', '.join([str(pts) for pts in self._pts])
        return f"Polygon({ptr_str})"

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError("Can only concatenate with another Polygon")

    def __iadd__(self, other):
        
        if isinstance(other, Polygon):
            points = other._pts
        else:
            pointts = [Points(*pt) for pt in other]
        self._pts = self._pts + points
        return self._pts
        

p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))


print(id(p1), p1)

p1 += p2

print(id(p1), p1)

            
    





