import unittest

import trapezoid


class TrapezoidTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(trapezoid.area(10, 4, 4), 28)

    def test_perimeter(self):
        self.assertEqual(trapezoid.perimeter(10, 4, 5, 5), 24)
