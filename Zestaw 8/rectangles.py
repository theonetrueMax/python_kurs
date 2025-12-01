from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates: must satisfy x1 < x2 and y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
       
        if len(points) != 2:
            raise ValueError("Należy podać dokładnie dwa punkty.")
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)

    # ---------- KONWERSJE TEKSTOWE ----------
    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    # ---------- PORÓWNANIA ----------
    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    # ---------- WIRTUALNE ATRYBUTY LICZBOWE ----------
    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def top(self):
        return self.pt2.y

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def topright(self):
        return self.pt2

    @property
    def center(self):
        return Point(
            (self.left + self.right) / 2,
            (self.bottom + self.top) / 2,
        )
    def area(self):
        return self.width * self.height

    def move(self, dx, dy):
        return Rectangle(
            self.left + dx,
            self.bottom + dy,
            self.right + dx,
            self.top + dy,
        )

'''
import pytest

if __name__ == "__main__":
    pytest.main(["-v"])

'''