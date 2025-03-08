# 2025.03.06
# Mavzu: OOP (Mavzu)
# Muallif: Muhammadsodiq

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def get_lastname(self, familiya):
        return self.familiya
    
    def get_age(self, yil = 2025):
        return yil - self.tyil

    def tanishtir(self):
        print(f"Ismim {self.ism}, familiyam {self.familiya}. Tug'ilgan yilim {self.tyil}")

talaba1 = Talaba("Olim", 'Komilov', 2002)
talaba2 = Talaba("Hasan", 'Alimov', 2003)

print(talaba1.__dict__)
print(talaba2.__dict__)