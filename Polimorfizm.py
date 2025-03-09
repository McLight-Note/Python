# 2024.03.07
# Mavzu: Polimorfizm
# Muallif: Muhammadsodiq

class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self. passport = passport
        self.tyil = tyil
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}"
        info += f"Pasport: {self.passport}, {self.tyil}"
        return get_info
    
    def get_age(self, yil):
        return yil - self.tyil

class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, idraqam, manzili, tyil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1

    def get_id(self):
        return self.idraqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}"
        info += f"{self.get_bosqich()} - bosqich. ID - {self.idraqam}"
        return info

class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani"
        manzil += f"{self.kocha} ko'chasi, {self.uy} - uy"
        return manzil
    
talaba1_manzil = Manzil(12,'Olmazor','Oltinkol','Andijon')
talaba1 = Talaba('Alijon', 'Valiyev','FF112233', 'NA0000012', talaba1_manzil, 2000)

print(talaba1.get_info())