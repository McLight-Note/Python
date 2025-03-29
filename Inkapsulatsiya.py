# 2025.03.29
# Mavzu: Inkapsulatsiya
# Muallif: Muhammadsodiq

from uuid import uuid4

class Avto:
    __num_avto = 0
    PI = 3.14159

    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >=0:
            self.__km += km
        else:
            print(f"Mashina km kamaytirib bo'lmaydi")
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

class Bus:
    pass

class Train:
    pass

avto1 = Avto("GM", "MaLibu", "Qora", 2020, 40000, 1000)
avto2 = Avto("Porsche", "Supra", "Qizil", 2025, 250000, 1200)
avto3 = Avto("Mustang", "Challenger", "oq", 2026, 340000, 1500)
print(avto1.narh)
print(avto1.get_id())
print(avto1.get_km())
print(avto1.add_km(2000))
print(avto1.get_km())
print(avto1.add_km(-2000))
print(Avto.get_num_avto())