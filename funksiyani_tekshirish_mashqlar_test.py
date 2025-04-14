# 2025.04.14
# Mavzu: Funksiyani tekshish Mashqlar
# Muallif: MUhammadsodiq

import unittest
from funksiyani_tekshirish_mashqlar import *

class mashqTest(unittest.TestCase):
    def test_big_number(self):
        self.assertEqual(biggest_number(14, 432, 12), 432)
    
    def test_str_changer(self):
        self.assertEqual(str_changer(['olma', 'nok', 'behi']), ['Olma', 'Nok', 'Behi'])

    def test_even_number(self):
        self.assertEqual(even_number([1,2,3,4,5,6,7,8,9,10]), [2,4,6,8,10])

    def test_fibonacci(self):
        self.assertEqual(fibda_bormi(10), False)

unittest.main()