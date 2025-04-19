# 2025.04.18
# Mavzu: Testing Mashqlar
# Muallif: Muhammadsodiq

import unittest
from Polimorfizm_takrorlash import Shaxs, Talaba, Manzil

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        self.ism = 'Abdulloh'
        self.familiya = 'Otamirzayev'
        self.passport = 'fa1212313'
        self.tyil = 2006

        self.odam1 = Shaxs(self.ism, self.familiya, self.passport, self.tyil)
        self.odam2 = Shaxs(self.ism, self.familiya, self.passport, self.tyil)
    
    def test_create(self):
        self.assertIsNotNone(self.odam1.ism)
        self.assertIsNotNone(self.odam2.ism)
        self.assertIsNotNone(self.odam1.familiya)
        self.assertIsNotNone(self.odam2.familiya)
        self.assertIsNotNone(self.odam1.passport)
        self.assertIsNotNone(self.odam2.passport)
        self.assertEqual(self.odam2.tyil, self.tyil)

    def test_get_age(self):
        new_year = 2025
        self.assertEqual(self.odam1.get_age(new_year), 19)
    
class TalabaTest(unittest.TestCase):
    def setUp(self):
        self.ism = 'Abdu'
        self.familiya = 'Orzayev'
        self.passport = 'fa1212313'
        self.tyil = 2014
        self.idraqam = 'n001'
        self.bosqich = 1

        self.talaba1 = Talaba(self.ism, self.familiya, self.passport, self.tyil, self.idraqam, manzil=None)
        self.talaba2 = Talaba(self.ism, self.familiya, self.passport, self.tyil, self.idraqam, manzil=None)
    
    def test_create(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba2.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba2.familiya)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba2.tyil)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba2.passport)
        self.assertIsNotNone(self.talaba2.idraqam)
        self.assertEqual(self.talaba1.tyil, self.tyil)
        self.assertEqual(self.talaba2.tyil, self.tyil)
        self.assertEqual(self.talaba1.passport, self.passport)
    
    def test_get_id(self):
        self.assertEqual(self.talaba1.get_id(), self.idraqam)
        self.assertEqual(self.talaba2.get_id(), self.idraqam)
    
    def test_get_bosqich(self):
        self.assertEqual(self.talaba1.get_bosqich(), self.bosqich)
        self.assertEqual(self.talaba2.get_bosqich(), self.bosqich)

        new_bosqich = 4
        try:
            self.talaba1.get_bosqich(new_bosqich)
            self.assertEqual(self.talaba1.get_bosqich(new_bosqich), 4)
        except TypeError as error:
            self.assertEqual(type(error), TypeError)
            print(f'{self.talaba1.familiya.title()} {self.talaba1.ism.title()} gayangi bosqich bera olmaysiz!')
        
        try:
            self.talaba1.get_bosqich(new_bosqich)
            self.assertEqual(self.talaba2.get_bosqich(new_bosqich), 4)
        except TypeError as error:
            self.assertEqual(type(error), TypeError)
            print(f'{self.talaba2.familiya.title()} {self.talaba2.ism.title()} ga yangi bosqich bera olmaysiz!')

    def test_get_info(self):
        self.assertEqual(self.talaba1.get_info(), f'{self.ism.title()} {self.familiya.title()}\n' + f'{self.passport}, {self.tyil} - yilda tugilgan.\nID: {self.idraqam}\n{self.bosqich} - yil talabasi\n\n')
        self.assertEqual(self.talaba2.get_info(), f'{self.ism.title()} {self.familiya.title()}\n' + f'{self.passport}, {self.tyil} - yilda tugilgan.\nID: {self.idraqam}\n{self.bosqich} - yil talabasi\n\n')

class YagonaTest(unittest.TestCase):
    def setUp(self):
        self.manzil = Manzil(10, "Bogbon", "Chust", "Namangan")
        self.shaxs = Shaxs("Aziz", "Bekov", "AA1234567", 1995)
        self.talaba = Talaba("Ali", "Valiyev", "BB7654321", 2002, "T1001", self.manzil)
    
    def test_instance_types(self):
        self.assertTrue(isinstance(self.shaxs, Shaxs))
        self.assertTrue(isinstance(self.talaba, Talaba))
        self.assertTrue(isinstance(self.talaba, Shaxs))
        self.assertTrue(isinstance(self.manzil, Manzil))
    
    def test_get_info_polymorphism(self):
        shaxs_info = self.shaxs.get_info()
        talaba_info = self.talaba.get_info()
        
        self.assertIn("Aziz", shaxs_info)
        self.assertIn("Ali", talaba_info)
        self.assertIn("T1001", talaba_info)

    def test_manzil_class(self):
        full_address = self.manzil.get_manzil()
        self.assertIn("Namangan", full_address)
        self.assertIn("Chust", full_address)
        self.assertIn("Bogbon", full_address)
    
    def test_age_calculation(self):
        self.assertEqual(self.shaxs.get_age(2025), 30)
        self.assertEqual(self.talaba.get_age(2025), 23)

unittest.main()