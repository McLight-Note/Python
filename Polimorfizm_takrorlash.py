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
    
inson = Shaxs("alisher", 'toraboyev', "AC2988913", 1997)
print(f"{inson.get_info()}, {inson.get_age(2025)} yoshda")