# 2025.03.20
# Mavzu: Takrorlash OOP Mashqlar
# Muallif: Muhammadsodiq

import math

class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 500
    
    def get_model(self):
        return self.model.title()

    def get_color(self):
        return self.rang.title()

    def get_car_type(self):
        return self.korobka.title()

    def get_price(self):
        return self.narh
    
    def get_milage(self):
        return self.kilometr
    
    def update_milage(self):
        self.kilometr += 100
        return self.kilometr
    
    def get_info(self):
        return f"{self.model} moshinasi {self.rang} rangli. Narhi = {self.narh}, turi {self.korobka} va {self.kilometr} km yurgan"
    
class Avtosalon:
    def __init__(self, salon_nomi, manzili, mavjud_avtolar=None):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.mavjud_avtolar = mavjud_avtolar if mavjud_avtolar is not None else []
    
    def get_name(self):
        return self.salon_nomi.title()
    
    def get_adress(self):
        return self.manzili.title()
    
    def get_cars(self):
        return [car.get_info() for car in self.mavjud_avtolar]
    
    def add_cars(self, added_car):
        self.mavjud_avtolar.append(added_car)
    
def see_method(klass):
    return (method for method in dir(klass) if method.startswith('__') is False)

# Avtomobillar yaratamiz
avto1 = Avto('Malibu', 'kok', 'avtomat', 2000)
avto2 = Avto('Nexia', 'qizil', 'mexanik', 2024)

# Avtosalon obyektini yaratamiz va avto1 ni ro‘yxatga qo‘shamiz
avto_salon = Avtosalon('Toshkent Avtosaloni', 'Qoshariq', [avto1])

# Yangi avtomobil qo‘shamiz
avto_salon.add_cars(avto2)

# Natijalarni chop etamiz
print(avto1.get_info())
print(avto_salon.get_cars())
print(dir(Avtosalon))
print(avto1.__dict__.keys())
print(see_method(Avto))
print(see_method(Avtosalon))