# 2025.03.30
# Mavzu: Inkapsulatsiya
# Muallif: Muhammadsodiq

from uuid import uuid4

class Shaxs:
    __shaxs_soni = 0
    
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        Shaxs.__shaxs_soni += 1

    def get_age(self, yil):
        return yil - self.tyil
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil} yilda tvallud topgan\n"
        return info
    
    @classmethod
    def get_num_person(cls):
        return cls.__shaxs_soni

class Talaba(Shaxs):
    __talaba_soni = 0

    def __init__(self, ism, familiya, tyil, idraqam, passport):
        super().__init__(ism, familiya, tyil)
        self.__idraqam = uuid4()
        self.__passport = passport
        Talaba.__talaba_soni += 1
        self.bosqich = 2
    
    def get_id(self):
        return self.__idraqam
    
    def get_passport(self):
        return self.__passport
    

    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil} yilda tvallud topgan\n{self.bosqich}-kurs"
        return info
    
    @classmethod
    def get_num_students(cls):
        return cls.__talaba_soni

talaba1 = Talaba('Abdulloh', 'Otamirzayev', 2006, '20247388', 'FA361523')
talaba2 = Talaba('Buhor', 'Oliyev', 2016, '2024345345', 'FA362343')
talaba3 = Talaba('Narrwet', 'Merayev', 2006, '202412412', 'FA36233')
print(talaba1.get_info())
print(talaba1.get_id())