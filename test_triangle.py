import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_for_sides_3_4_5(self):
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6, places=7)

    def test_perimeter_for_sides_3_4_5(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
