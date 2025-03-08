# 2025.03.06
# Mavzu: OOP (Mashqlar)
# Muallif: Muhammadsodiq

from datetime import date, datetime

class Web:


    def __init__(self, ism: str, familiya: str, tyil: int):
        self.name = ism
        self.surname = familiya
        self.born = tyil
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_age(self, yil = 2025):
        return yil - self.born
    
    def get_info(self):
        print(f"Foydalanuvchi {self.name}{self.born}\n {self.name.upper()} {self.surname.upper()}, {self.born } yilda tug'ilganman")


new_web = Web("Yusufjon", "Akhmedov", 2004)
print(new_web.get_info())