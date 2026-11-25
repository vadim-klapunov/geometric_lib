import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_for_sides_3_and_4(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_perimeter_for_sides_3_and_4(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)
