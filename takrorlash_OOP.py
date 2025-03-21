# 2025.03.19
# Mavzu: Takrorlash OOP
# Muallif: Muhammadsodiq

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        self.bosqich += 1

    def get_info(self):
        return f"{self.ism.title()} {self.familiya.title()}. {self.bosqich}-bosqich talabasi"

    def get_name(self):
        return self.get_name.title()
    
    def get_lastname(self):
        return self.familiya.title()
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
    
class Fan():
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_name(self):
        return self.nomi.title()

    def get_students(self):
        """talabalar = []
        for talaba in self.talabalar:
            talabalar.append(talaba.get_fullname())
        return talabalar"""
        return [talaba.get_fullname() for talaba in self.talabalar]

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

talaba1 = Talaba('Alisher', 'Valiyev', 1992)
talaba2 = Talaba('Bmw', 'aliyev', 2000)

matem = Fan('Oliy Matemaika')
matem.add_student(talaba1)
matem.add_student(talaba2)
print(talaba1.bosqich)
print(matem.talabalar[0].get_info())

matematika = Fan("OLiy Matematika")
talabal = Talaba("ALijon", "Valiyev", 2000)
talaba2 = Talaba ( "Hasan", "Alimov", 2001)
talaba3 = Talaba ("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.get_students())
print(dir(Talaba))
print(talaba1.__dict__)
print(talaba1.__dict__.keys())
print(see_methods(Talaba))