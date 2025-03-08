# 2025.03.07
# Mavzu: OOP. Obyektlar bilan ishlash Mashqlar
# Muallif: Muhammadsodiq

class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 5000
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.rang
    
    def get_type(self):
        return self.korobka
    
    def get_price(self):
        return self.narh
    
    def get_milage(self):
        return self.kilometr
    
    def get_info(self):
        print(f"{self.rang.upper()} rangli {self.model.upper()} avtomashinasi"
                f"\n{self.korobka} holatda va narhi {self.narh}$")
    
    def update_km(self):
        self.kilometr += 100
    
class Avtosalon:
    def __init__(self, nomi, manzili, avtomobillar):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = avtomobillar
        self.avtomobillar_soni = 0
        self.avtomobillar_yigimi = []
    
    def get_name_salon(self):
        return self.nomi
    
    def get_adress(self):
        return self.manzili
    
    def get_cars(self):
        self.avtomobillar
    
    def add_cars(self, moshina):
        self.avtomobillar_yigimi.append(moshina)
        self.avtomobillar_soni += 1
    
    def get_salon_info(self):
        print(f"Salon nomi - {self.nomi.upper()}\n"
              f"Manzili - {self.manzili.upper()}"
              f"Mavjud avtomobillar - {self.avtomobillar_yigimi}")

car1 = Avto("Tesla Model S", "oq", "avtomat", 80000)
car2 = Avto("BMW X5", "qora", "avtomat", 60000)
car3 = Avto("Chevrolet Malibu", "ko'k", "avtomat", 25000)

salon = Avtosalon("Premium Avtosalon", "Toshkent", [])
salon.add_cars(car1)
salon.add_cars(car2)
salon.add_cars(car3)

car1.get_info()
car2.get_info()
car3.get_info()

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

def see_method(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

