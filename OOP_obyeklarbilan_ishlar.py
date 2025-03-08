# 2024.03.06
# Mavzu: OOP (Obyektlar bilan ishlash)
# Muallif: Muhammadsodiq

from datetime import date

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_name(self):
        return self.ism.upper()
    
    def get_lastname(self):
        return self.familiya.upper()
    
    def get_age(self):
        return 2025 - self.tyil
    
    def get_info(self):
        print(f"Mening ismim {self.ism.upper()}"
              f"\nFamiliyam {self.familiya.upper()}"
              f"\nYoshim {2025 - self.tyil}")
    
    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich
    
    def update_bosqich(self, update_bosqich):
        self.bosqich += 1
    
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_students(self,):
        return [talaba.get_info() for talaba in self.talabalar]

matematika = Fan("OLiy Matematika")
talaba1 = Talaba ("Alijon", "Valiyev", 2000)
talaba2 = Talaba ( "Hasan", "Alimov", 2001)
talaba3 = Talaba ( "Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.get_students())

def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]
    
print(see_methods(Talaba))
print(see_methods(Fan))
print(talaba1.__dict__)
print(see_methods(talaba1))