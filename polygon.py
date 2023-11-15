## Project Info

"""
Polygons:
1. Initializer number of edges/vertes and circumradius

properties:
1. edges
2. vertices
3. interior angle
4. apothem
5. area
6. perimeter
"""
import math

class Polygon:

    def __init__(self, n, R):
        self._n = n
        self._R = R

    def __repr__(self):
        return f"Polygon(n={self._n}, R={self._R})"

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * 180/ n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi /self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n/2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        self._n * self.side_length



def test_polygon():
    n = 3
    R = 1
    p = Polygon(n, R)
    print(p)

    assert str(p) == f"Polygon(n=3, R=1)", f"actual: {str(p)}"
    assert p.count_vertices == n
    assert p.circumradius == R
    assert round(p.area) == 1

test_polygon() 
