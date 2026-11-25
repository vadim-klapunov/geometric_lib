import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_area_for_radius_3(self):
        self.assertAlmostEqual(circle.area(3), 28.2743338823, places=7)

    def test_perimeter_for_radius_3(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.8495559215, places=7)
