# 2025.04.18
# Mavzu: Klassni tekshirish test
# Muallif: Muhammadsodiq

import unittest
from klassni_tekshirish import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.make = 'GM'
        self.model = 'Malibu'
        self.year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(self.make, self.model, self.year)
        self.avto2 = Car(self.make, self.model, self.year, price=self.price)

    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        self.assertIsNone(self.avto1.price)
        self.assertEqual(0,self.avto1.get_km())
        self.assertEqual(self.price, self.avto2.price)

    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(self.avto2.price, new_price)
    
    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.avto1.get_km(), self.km)
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km())
        
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)


unittest.main()