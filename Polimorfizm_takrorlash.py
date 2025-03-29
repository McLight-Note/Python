# 2025.03.21
# Mavzu: Polimorfizm takrorlash
# Muallif: Muhammadsodiq

class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        return yil - self.tyil
    
class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f'{self.ism.title()} {self.familiya.title()}\n'
        info += f'{self.passport}, {self.tyil} - yilda tugilgan.\nID: {self.idraqam}\n{self.bosqich} - yil talabasi\n\n'
        return info

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzil = f"{self.viloyat.title()} viloyati, {self.tuman.title()} tumani\n"
        manzil += f"{self.kocha.title()} kochasi {self.uy}-uy"
        return manzil

talaba1_manzil = Manzil(1, 'Navbahor', 'Uychi', 'Namangan')
print(talaba1_manzil.get_manzil())

talaba1 = Talaba('alijon', 'qoziyev', 'FA2020202', 2000, 'n001', talaba1_manzil)
print(talaba1.get_info())
print(talaba1.get_age(2025), 'yoshda')
print(talaba1.get_id())
inson = Shaxs("alisher", 'toraboyev', "AC2988913", 1997)
print(f"{inson.get_info()}, {inson.get_age(2025)} yoshda")
print(talaba1.manzil.get_manzil())