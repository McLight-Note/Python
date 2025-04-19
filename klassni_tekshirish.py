# 2025.04.18
# Mavzu: Klassni tekshirish
# Muallif: Muhammadsodiq

class Car:
    def __init__(self, make, model, year, km = 0, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
    
    def set_price(self, a):
        self.price = a
    
    def add_km(self, a):
        if a>=0:
            self.__km += a
        else:
            raise ValueError('Manfiy bolishi mumkin emas!')
    
    def get_info(self):
        info = f"{self.make.title()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km} km yurgab"
        if self.price:
            info += f"Narhi {self.price}"
        
        return info

    def get_km(self):
        return self.__km
    