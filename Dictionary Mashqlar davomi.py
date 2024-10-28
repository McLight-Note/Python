# 29.10.2024
# Dictinary Davomi mashqlar
# Muallif: Muhammadsodiq

import math

"""lugat = {
    'integer': 'Butun son',
    'float': "O'nlik son",
    'boolean': 'Mantiqiy qiymat',
    'for': 'Amalni qayta bajarish tsikli',
    'if': 'Shartni tekshirish operatori',
    'else': 'Shartni davomini tekshirish operatori',
    'elif': 'Shartga qoshimcha qoshish'
}

for key, value in sorted(lugat.items()):
    print(f"{key.title()} -- {value}")"""

"""davlatlar = {
    'AQSh': '      Washington',
    'Italiya': '   Rim',
    'Ozbekiston': 'Toshkent',
    'Tojikiston': 'Dushanbe',
    'Qozogiston': 'Nursulton',    
    'Singapur': '  Singapur',
    'Rossiya': '   Moskva',
    'Fransiya': '  Paris'
}

print('Dunyo davlatlari: Dunyo poytaxtlari')
for k,q in sorted(davlatlar.items()):
    print(f'{k} --- {q}')"""

"""for k,q in davlatlar.items():
    x = input('Qaysi davlatni poytaxtini bilishni xoxlaysiz? >>>> ')
    if x in k:
        print(f"{x} poytaxti {q} shahri!")
    else:
        print('Bu haqida malumot yoq')"""

"""davlat = input('Qaysi davlat poytaxtini bilishni xoxlaysi? >>>')
poytaxt = davlatlar.get(davlat)
if poytaxt == None:
    print('Bu haqida malumot yoq')
else:
    print(f'{davlat} poytaxti {poytaxt} shahri')"""

"""taomlar = {
    'osh':10000,
    'shorva':12000,
    'manti':3000,
    'choy':5000,
    'qatiq':7000,
    'non':3000,
    'baliq':15000,
    'nonshorva':8000,
    'shashlik':12000
}
print('3 ta taom buyurtma bering!')
buyurtmalar = []
hisob = 0
for a in range(3):
    buyurtmalar.append((input(f"{a + 1}-taom:").lower()))

for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma} {taomlar[buyurtma]} som")
        hisob = hisob + taomlar[buyurtma]
    else:
        print(f'Kechirasiz bizda {buyurtma} yoq!')
print(f'Jami: {hisob} som')"""