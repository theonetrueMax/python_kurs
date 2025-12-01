from points import Point
import unittest

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates: must satisfy x1 < x2 and y1 < y2")
        self.pt1 = Point(x1, y1)  
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return (
            isinstance(other, Rectangle) and
            self.pt1 == other.pt1 and
            self.pt2 == other.pt2
        )

    def __ne__(self, other):
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, dx, dy):
        return Rectangle(
            self.pt1.x + dx, self.pt1.y + dy,
            self.pt2.x + dx, self.pt2.y + dy
        )

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Rectangles do not intersect")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2

        r1 = Rectangle(self.pt1.x, self.pt1.y, cx, cy)
        r2 = Rectangle(cx, self.pt1.y, self.pt2.x, cy)
        r3 = Rectangle(self.pt1.x, cy, cx, self.pt2.y)
        r4 = Rectangle(cx, cy, self.pt2.x, self.pt2.y)

        return (r1, r2, r3, r4)


class TestRectangle(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 5, 0)
        
        Rectangle(0,1, 2, 3)

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
        self.assertEqual(r.area(), 12)
        self.assertNotEqual(r.area(), 1)

    def test_move(self):
        r = Rectangle(0, 0, 2, 2)
        moved = r.move(3, 4)
        self.assertEqual(moved, Rectangle(3, 4, 5, 6))
        self.assertNotEqual(r, Rectangle(0, 0, 1, 1))


    def test_intersection(self):
        r1 = Rectangle(0, 0, 4, 4)
        r2 = Rectangle(2, 2, 6, 6)
        inter = r1.intersection(r2)
        self.assertEqual(inter, Rectangle(2, 2, 4, 4))

    def test_intersection_empty(self):
        r1 = Rectangle(0, 0, 2, 2)
        r2 = Rectangle(3, 3, 4, 4)
        with self.assertRaises(ValueError):
            r1.intersection(r2)

    def test_cover(self):
        r1 = Rectangle(0, 0, 1, 1)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(
            r1.cover(r2),
            Rectangle(0, 0, 4, 5)
        )

    def test_make4(self):
        r = Rectangle(0, 0, 4, 4)
        q1, q2, q3, q4 = r.make4()
        self.assertEqual(q1, Rectangle(0, 0, 2, 2))
        self.assertEqual(q2, Rectangle(2, 0, 4, 2))
        self.assertEqual(q3, Rectangle(0, 2, 2, 4))
        self.assertEqual(q4, Rectangle(2, 2, 4, 4))


if __name__ == "__main__":
    unittest.main()