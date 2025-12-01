import pytest
from rectangles import Rectangle
from points import Point

def test_from_points():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    r = Rectangle.from_points((p1, p2))
    assert r.left == 1
    assert r.bottom == 2
    assert r.right == 4
    assert r.top == 6

def test_properties():
    r = Rectangle(0, 0, 3, 4)
    assert r.width == 3
    assert r.height == 4
    assert r.topleft == Point(0, 4)
    assert r.bottomright == Point(3, 0)

def test_center():
    r = Rectangle(0, 0, 4, 4)
    assert r.center == Point(2, 2)

def test_area():
    r = Rectangle(2, 3, 5, 7)
    assert r.area() == 12

def test_move():
    r = Rectangle(1, 1, 3, 3)
    moved = r.move(10, -5)
    assert moved == Rectangle(11, -4, 13, -2)

def test_str_repr():
    r = Rectangle(1, 2, 3, 4)
    assert str(r) == "[(1, 2), (3, 4)]"
    assert repr(r) == "Rectangle(1, 2, 3, 4)"

def test_invalid():
    with pytest.raises(ValueError):
        Rectangle(5, 5, 2, 3)