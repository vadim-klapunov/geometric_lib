import unittest

import square


class SquareTestCase(unittest.TestCase):
    def test_area_for_side_5(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter_for_side_5(self):
        self.assertEqual(square.perimeter(5), 20)
