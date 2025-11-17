
from math import gcd

def normalize(frac):
    "Zwraca ułamek w postaci [a, b] z b > 0 i gcd(a,b)=1"
    num, den = frac
    if den == 0:
        raise ZeroDivisionError("Mianownik nie może być zerem")

    # przeniesienie minusa na licznik
    if den < 0:
        num = -num
        den = -den

    if num == 0:
        return [0, 1]

    g = gcd(num, den)
    return [num // g, den // g]


def add_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return normalize([a * d + b * c, b * d])


def sub_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return normalize([a * d - b * c, b * d])


def mul_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return normalize([a * c, b * d])


def div_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    if c == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    return normalize([a * d, b * c])


def is_positive(frac):
    num, den = normalize(frac)
    return num > 0


def is_zero(frac):
    num, den = normalize(frac)
    return num == 0


def cmp_frac(frac1, frac2):
    a, b = frac1
    c, d = frac2
    left = a * d
    right = b * c
    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0


def frac2float(frac):
    num, den = frac
    return num / den




import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
    
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [4, 8]), [1, 1])
        self.assertEqual(add_frac([1, 6], [-3, 6]), [-1, 3])
        self.assertEqual(add_frac([-13, 5], [15, 2]), [49, 10])
    
    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 6]), [1, 3])
        self.assertEqual(sub_frac([3, 5], [-1, 10]), [7, 10])
        self.assertEqual(sub_frac([-4, 7], [-2, 14]), [-3, 7])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([2, 3], [0, 4]), [0, 1])
        self.assertEqual(mul_frac([5, 2], [2, 5]), [1, 1])
        self.assertEqual(mul_frac([3, 4], [5, 6]), [5, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 3], [3, 4]), [8, 9])
        self.assertEqual(div_frac([5, 2], [5, 2]), [1, 1])
        self.assertEqual(div_frac([3, 4], [6, 5]), [5, 8])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertTrue(is_positive([-11, -52]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 5]))
        self.assertTrue(is_zero([0, -7]))
        self.assertFalse(is_zero([1, 2]))
        self.assertTrue(is_zero([-0, 5]))
        self.assertFalse(is_zero([-1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([3, 2], [1, 2]), 1)
        self.assertEqual(cmp_frac([-3, 2], [1, 2]), -1)
        self.assertEqual(cmp_frac([-3, 2], [3, -2]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([5, 9]), 0.55555555)
        self.assertAlmostEqual(frac2float([65, 10]), 6.5)
        self.assertAlmostEqual(frac2float([-0, 1]), -0.0)
        self.assertAlmostEqual(frac2float([-3, -5]), 0.6)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy