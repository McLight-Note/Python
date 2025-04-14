# 2025.04.14
# Mavzu: Test dasturi uchun
# Muallif: Muhammadsodiq

import unittest

from funksiyani_tekshirish import get_full_name

class Funksiyani_tekshirish(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon', 'valiyev')
        self.assertEqual(name, 'Alijon Valiyev')
    
    def test_otasining_ismi(self):
        name = get_full_name('alijon', 'valiyev', 'olimovich')
        self.assertEqual(name, 'Alijon Olimovich Valiyev')

unittest.main()