# 2025.03.30
# Mavzu: Dunder metolar Mashqlar
# Muallif: Muhammadsodiq

from uuid import uuid4

class Shaxs:
    __shaxs_soni = 0

    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        Shaxs.__shaxs_soni += 1
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil}-yilad tavallud topgan"
        return info
    
    def __lt__(self, boshqa_odam):
        return self.tyil < boshqa_odam.tyil
    
class Talaba(Shaxs):
    def __init__(self, ism, familiya, tyil, idraqam, passport, bosqich):
        super().__init__(ism, familiya, tyil)
        self.idraqam = uuid4()
        self.passport = passport
        self.talabalar = []
        self.bosqich = bosqich
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}"
        info += f"\n{self.bosqich}-kurs"
        return info
    
    def __repr__(self):
        return f"{self.ism.title()} {self.familiya.title()}\n{self.tyil}\n{self.idraqam}\n{self.passport}"

    def __add__(self, boshqa_odam):
        if isinstance(boshqa_odam, Talaba):
            yangi_guruh = Talaba(f"{self.ism} -- {boshqa_odam.ism}", f'{self.familiya} -- {boshqa_odam.familiya}', f"{self.tyil} -- {boshqa_odam.tyil}", f'ID:{self.idraqam}\n{boshqa_odam.idraqam}',f"Passportlari: {self.passport} -- {boshqa_odam.passport}", f'{self.bosqich} -- {boshqa_odam.bosqich}')
            yangi_guruh.talabalar = self.talabalar + boshqa_odam.talabalar
            return yangi_guruh
        elif isinstance(boshqa_odam, Talaba):
            self.add_talaba(boshqa_odam)

    def add_talaba(self, boshqa_odam):
        for talaba in boshqa_odam:
            if isinstance(talaba, Shaxs):
                self.talabalar.append(talaba)
            else:
                print('Talaba kiriting')

    def bosqichi(self, boshqa_odam):
        return self.bosqich < boshqa_odam.bosqich

class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.fan_talabalari = []
    
    def __getitem__(self, index):
        return self.fan_talabalari[index]
    
    def __setitem__(self, index, boshqa_odam):
        self.fan_talabalari[index] = boshqa_odam
    
    def __len__(self):
        return len(self.fan_talabalari)
    
    def __sub__(self, boshqa_odam):
        if isinstance(boshqa_odam, Fan):
            yangi_fan = Fan(f"{self.nomi} - {boshqa_odam.nomi}")
            yangi_fan.fan_talabalari = [talaba for talaba in self.fan_talabalari if talaba not in boshqa_odam.fan_talabalari]
            return yangi_fan
        else:
            raise ValueError("Faqat Fan obyektlarini ayrish mumkin")
    
    def sub_student(self, boshqa_odam):
        if isinstance(boshqa_odam, Talaba):
            self.fan_talabalari.remove(boshqa_odam)
        else:
            raise ValueError('Faqat Talaba obyektlarini ayrish mumkin')
    
    def __add__(self, boshqa_odam):
        if isinstance(boshqa_odam, Fan):
            yangi_fan = Fan(f"{self.nomi} & {boshqa_odam.nomi}")
            yangi_fan.fan_talabalari = self.fan_talabalari + boshqa_odam.fan_talabalari
            return yangi_fan
        else:
            raise TypeError("Faqat Fan obyektlarini qo'shish mumkin")

    def add_student(self, talaba):
        if isinstance(talaba, Talaba):
            self.fan_talabalari.append(talaba)
        else:
            raise ValueError("Faqat Talaba obyektlarini qo'shish mumkin")

talaba1 = Talaba("Abdullo", "Rojiyev", 2004, "#002", "AC123123", 5)
talaba2 = Talaba("Oyatullo", "Qoziyev", 2003, "#005", "AC323232", 3)
talaba3 = Talaba("Yusuf", "Qoriyev", 2004, "#013", "AC424223", 4)
talaba4 = Talaba("Shoyat", "Albekov", 2000, "#004", "AC345234", 1)
talaba5 = Talaba("Nemat", "Choriyev", 1989, "#008", "AC876544", 2)
talaba6 = Talaba("Shokir", "Zariveov", 1998, "#09", "AC434432", 3)

matem = Fan("Matematika")
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba4)

fizika = Fan("Fizika")
fizika.add_student(talaba3)
fizika.add_student(talaba5)

geografiya = Fan("Geografiya")
geografiya.add_student(talaba2)
geografiya.add_student(talaba5)
geografiya.add_student(talaba6)
geografiya.add_student(talaba3)

birlashtirilgan_fan1 = matem + fizika
birlashtirilgan_fan2 = matem + geografiya

print(f"{matem.nomi} fanida {len(matem)} ta talaba bor")
print(f"{fizika.nomi} fanida {len(fizika)} ta talaba bor")
print(f"{geografiya.nomi} fanida {len(geografiya)} ta talaba bor")
print(f"{birlashtirilgan_fan1.nomi} fanida {len(birlashtirilgan_fan1)} ta talaba bor")
print(f"{birlashtirilgan_fan2.nomi} fanida {len(birlashtirilgan_fan2)} ta talaba bor")

ayrish_fanlari1 = birlashtirilgan_fan2 - matem
ayrish_fanlari2 = birlashtirilgan_fan1 - fizika

print(f"{birlashtirilgan_fan1.nomi} fanida {len(birlashtirilgan_fan1)} ta talaba bor edi >>>")
print(f"Endi {geografiya.nomi} fanida {len(ayrish_fanlari1)} ta talaba bor")
print(f"{birlashtirilgan_fan2.nomi} fanida {len(birlashtirilgan_fan2)} ta talaba bor edi >>>")
print(f"Endi {matem.nomi} fanida {len(ayrish_fanlari2)} ta talaba bor")