# 26.10.2024
# Mavzu: If va Else qoshmcha
# Muallif: Muhammdsodiq

import math

"""yosh = int(input('Yoshingiz nechchitda>>>'))

if yosh <= 4:
    print('sizga kirish bepul')
elif yosh <= 12:
    print('sizga kirish 5000')
elif yosh <= 18:
    print('kirish 8000')
else:
    print('sizga kirish 10000')"""

"""if yosh <= 4:
    narh = 0
elif yosh <= 12:
    narh = 5000
elif yosh <= 18:
    narh = 8000
else:
    narh = 10000

print(f'sizga krish {narh} som')"""

"""kun = input(" Bugun nima kun? >>>")
harorat = float(input('Bugun Havo qanday? >>>'))

if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat > 30:
    print('Bugun dam olish kuni va chomilgani ketdik!')
elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat <= 30:
    print('Bugun dam olish kuni lekn chomilgani bormaymiz...!')
else:
    print('bugun ish kuni')"""

"""if kun.lower() == 'yakshanba' and harorat > 30:
    print('Bugun dam olish kuni, chomilgani ketdik!')
elif kun.lower() == 'yakshanba' and harorat < 30:
    print('Uyda qolamiz!')"""

"""narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
print(narh)"""

"""if choy:
    print('Mijoz choy oldi.')
    narh = narh + 3000
if non:
    print('Mijoz non oldi.')
    narh = narh = 3000
if kompot:
    print('Mijoz kompot oldi.')
    narh = narh + 5000
if assorti:
    print('Mijoz assorti oldi.')
    narh = narh + 5000

print(f'Jami narh {narh} som bolidi.')"""

"""menu = ['somsa', 'osh', 'shashlik', 'kabob', 'qozonkabob', 'siltama', 'norin']
buyurtmalar = ['osh', 'somsa', 'manti', ' shashlik', 'shorva']"""

"""ovqat = input('Nima ovqat yeysiz? >>> ')

if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi')
else:
    print('Bizda bunday ovqat yo\'q')"""

"""if ovqat.lower() not in menu:
    print('Bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')"""

"""for taom in buyurtmalar:
    if taom in menu:
        print(f'Menuda {taom} bor')
    else:
        print(f"Menuda {taom} yoq!")"""

"""if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f'Menuda {taom} bor')
        else:
            print(f"Menuda {taom} yoq!")
else:
    print("Buyurtma bermadingiz!")"""

"""x = int(input('Juft son kiriting >>> '))
if x%2:
    print("Rahmat!")
else:
    print('Bu son juft emas!')"""

'''yosh = int(input('yoshingiz neccida? >>> '))
if yosh <= 4 or yosh >= 60:
    print("sizga kirish bepul")
elif yosh <= 18:
    print('Kirish 10000')
else:
    print('Kirish 20000')'''

'''x = int(input('x = '))
y = int(input('y = '))
if x == y:
    print("sonlar teng")
elif x < y:
    print('x<y')
else:
    print('x>y')'''

"""mahsulotlar = ['anor', 'uzum', 'olma', 'banan', 'nok', 'bodring', 'pomidor', 'tarvuz', 'shaftoli', 'olxori']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n + 1} - mahsulot qo'shing: "))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print('Dokonimizda bu mahsulot bor')
    else:
        print("Bizda bunday narsa yo'q")"""

"""mahsulotlar1 = ['anor', 'uzum', 'olma', 'banan', 'nok', 'bodring', 'pomidor', 'tarvuz', 'shaftoli', 'olxori']
bor_mahsulotlar = []
yoq_mahsulotlar = []

mahsulotlar = []
for n in range(5):
    mahsulotlar.append(input(f"{n + 1})Nima mahsulot olasz? >>> "))

for mahsulot in mahsulotlar:
    if mahsulot in mahsulotlar1:
        print(f"Do'konimizda {mahsulot} bor")
        bor_mahsulotlar.append(mahsulot)
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        yoq_mahsulotlar.append(mahsulot)

if len(yoq_mahsulotlar) == 0:
    print("Bizda hamma mahslotlar bor!")"""

"""foydalanuvchilar = ['anvar', 'behruz', 'zafar', 'lagan', 'tavoq']
x = input('Yangi login tanlang: ')

if x in foydalanuvchilar:
    print('Bu login band, boshqa tanlang')
else:
    print(f'Hush kelibsiz, {x.title()}')"""

sonlar = list(range(2, 11))
x = int(input('x = '))

for a in sonlar:
    if not(x%a):
        print(f" {x} soni {a} soniga bo'linadi!")
        