# 2025.04.14
# Mavzu: Funksiyani tekshirish
# Muallif: Muhammadsodiq

import unittest
from funk_tek import *

class funkTek(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975, 4)
        self.assertAlmostEqual(getArea(10), 314.159)
    
    def test_perimetr(self):
        self.assertEqual(getPerimetr(4), 25.13272)

unittest.main()