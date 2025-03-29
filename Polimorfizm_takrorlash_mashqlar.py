# 2025.03.29
# Mavzu: Polimorfizm takrorlash (Mashqlar)
# Muallif: Muhammadsodiq

class Shaxs:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        return self.ism
    
    def get_age(self, yil):
        return yil - self.tyil
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil} yilda tug'ilgan"
        return info

class Talaba(Shaxs):
    def __init__(self, ism, familiya, tyil, passport, idraqam):
        super().__init__(ism, familiya, tyil)
        self.passport = passport
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    
    def get_id(self):
        return self.idraqam
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil} yilda tug'ilgan\n{self.bosqich} - bosqich talabasi\n"
        info += f"Passport: {self.passport}\nID: {self.idraqam}"
        return info
    
    def fanga_yozil(self, fan):
        if fan in self.fanlar:
            print(f"Siz {fan} fanini olgansiz!")
        else:
            self.fanlar.append(fan)
        return self.fanlar

    def remove_fan(self, fan):
        if fan not in self.fanlar:
            print(f'Siz {fan} faniga yozilmagansiz!')
        else:
            self.fanlar.remove(fan)
        return self.fanlar

class Fanlar():
    def __init__(self, matematika, fizika, dasturlash, jistar):
        self.matematika = matematika
        self.fizika = fizika
        self.dasturlash = dasturlash
        self.jistar = jistar

class Professor(Shaxs):
    def __init__(self, ism, familiya, tyil, kasb):
        super().__init__(ism, familiya, tyil)
        self.kasb = kasb
    
    def get_kasb(self):
        return self.kasb
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil}-yilda tug'ilgan\n{self.kasb.title()} fanidan professor"
        return info

class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, tyil, kasb):
        super().__init__(ism, familiya, tyil)
        self.kasb = kasb
        self.narsalar = []
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil}-yilda tug'ilgan\n{self.kasb.title()} - kasb egasi"
        return info
    
    def add_narsa(self, narsa):
        if narsa not in self.narsalar:
            self.narsalar.append(narsa)
        else:
            print(f"Sizda {narsa} narsa bor")
    
    def remove_narsa(self, narsa):
        if narsa in self.narsalar:
            self.narsalar.remove(narsa)
        else:
            print(f'Sizda {narsa} yoq')
    
    def show_narsalar(self):
        print(f"Joriy narsalar: {', '.join(self.narsalar) if self.narsalar else 'Hech narsa yo\'q'}")

class Narsalar:
    def __init__(self, gosht, tuz, sut, shakar):
        self.gosht = gosht
        self.tuz = tuz
        self.shakar = shakar
        self.sut = sut

shaxs1 = Shaxs('Nozilbek', 'turdiyev', 1998)
print(shaxs1.get_info())

talaba1 = Talaba('qudrat', 'yolchiyev', 2003, 'FA293823023', 'N#001')
print(talaba1.get_info())

talaba1.fanga_yozil('Matematika')
print(talaba1.fanlar)

talaba1.fanga_yozil('Fizika') 
print(talaba1.fanlar) 

talaba1.fanga_yozil('Jismoniy Tarbiya')
print(talaba1.fanlar)

talaba1.fanga_yozil('Fizika')
print(talaba1.fanlar)

talaba1.remove_fan('Fizika')
print(talaba1.fanlar)

talaba1.remove_fan('Fizika')
print(talaba1.fanlar)

professor1 = Professor('bahodir', 'qoziyev', 1980, 'matematika')
print(professor1.get_info())

sotuvchi1 = Sotuvchi('Ali', 'Yusufov', 1990, 'Sotuvchi')
print(sotuvchi1.get_info())
sotuvchi1.add_narsa('Gosht')
sotuvchi1.add_narsa('Tuz')
print(sotuvchi1.show_narsalar())
sotuvchi1.remove_narsa('Tuz')
print(sotuvchi1.show_narsalar())

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, tyil):
        super().__init__(ism, familiya, tyil)
    
    def get_info(self):
        info = f"{self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.tyil}-yilda tug'ilgan\n"
        return info

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, tyil):
        super().__init__(ism, familiya, tyil)
        self.foydalanuvchilar = []
    
    def add_user(self, user):
        if user in self.foydalanuvchilar:
            print(f'{user.ism} foydalanuvchi bor')
        else:
            self.foydalanuvchilar.append(user)

    def ban_user(self, user):
        if user not in self.foydalanuvchilar:
            print(f'{user.ism} foydalanuvchi yoq')
        else:
            print(f'{user.ism} foydalanuvchi bloklandi')
            self.foydalanuvchilar.remove(user)
            
foydalanuvchi1 = Foydalanuvchi('Ali', 'Rahimov', 1995)
foydalanuvchi2 = Foydalanuvchi('Sami', 'Tashkentov', 1998)

print(foydalanuvchi1.get_info())
print(foydalanuvchi2.get_info())

admin1 = Admin('Zuhra', 'Gulomova', 1987)

admin1.add_user(foydalanuvchi1)
admin1.add_user(foydalanuvchi2)

print("Users in admin's list:")
for user in admin1.foydalanuvchilar:
    print(user.get_info())

admin1.add_user(foydalanuvchi1)
admin1.ban_user(foydalanuvchi1)

print("\nUsers in admin's list after banning:")
for user in admin1.foydalanuvchilar:
    print(user.get_info())