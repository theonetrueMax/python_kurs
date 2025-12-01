from points import Point
import unittest

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return (
            isinstance(other, Rectangle)
            and self.pt1 == other.pt1
            and self.pt2 == other.pt2
        )

    def __ne__(self, other):
        return not self == other

    def center(self):
        
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        
        width = abs(self.pt2.x - self.pt1.x)
        height = abs(self.pt2.y - self.pt1.y)
        return width * height

    def move(self, dx, dy):
       
        self.pt1 = Point(self.pt1.x + dx, self.pt1.y + dy)
        self.pt2 = Point(self.pt2.x + dx, self.pt2.y + dy)


class TestRectangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r), "[(1, 2), (3, 4)]")
        self.assertNotEqual(str(r), "[(3, 4), (1, 2)]")

    def test_repr(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(r), "Rectangle(1, 2, 3, 4)")
        self.assertNotEqual(repr(r), "[(3, 4), (1, 2)]")

    def test_eq(self):
        r1 = Rectangle(0, 0, 2, 2)
        r2 = Rectangle(0, 0, 2, 2)
        r3 = Rectangle(1, 1, 3, 3)
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 == r3)

    def test_ne(self):
        r1 = Rectangle(0, 0, 2, 2)
        r2 = Rectangle(0, 0, 2, 2)
        r3 = Rectangle(1, 1, 3, 3)
        self.assertFalse(r1 != r2)
        self.assertTrue(r1 != r3)

    def test_center(self):
        r = Rectangle(0, 0, 4, 4)
        self.assertEqual(r.center(), Point(2, 2))
        self.assertNotEqual(r.center(), Point(-2, -2))

    def test_area(self):
        r = Rectangle(1, 2, 4, 6)
        self.assertEqual(r.area(), (4 - 1) * (6 - 2))
        self.assertNotEqual(r.area(), 1)

    def test_move(self):
        r = Rectangle(0, 0, 2, 2)
        r.move(3, 4)
        self.assertEqual(r, Rectangle(3, 4, 5, 6))
        self.assertNotEqual(r, Rectangle(1, 1, 1, 1))

if __name__ == "__main__":
    unittest.main()