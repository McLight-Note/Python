# 2025.02.15
# Mavzu: Qiymat qaytaruvchi funksiya (Mashqlar)
# Muallif: Muhammadsodiq

import math

# 1,2 - mashqlar

"""
print('Odamlar qoshamiz')
odamlar = []

def shaxs_malumot(ism, familiya, tugilgan_yil, tel_raqam = ''):
    odam = {
        'ism': ism,
        'familiya': familiya,
        'tugilgan_yili': tugilgan_yil,
        'tel_raqam': tel_raqam}
    return odam

while True:
    ism = input('Ism: ')
    familiya = input('Familiya: ')
    tugilgan_yil = input('Tugilgan yili: ')
    tel_raqam = input('Telefon raqam: ')
        
    odamlar.append(shaxs_malumot(ism, familiya, tugilgan_yil, tel_raqam))

    javob = input('Davom etamizmi? (ha/yoq)')
    if javob.lower() == 'yoq':
        break

print("Siz qo'shgan odamlar ro'yxati")

for odam in odamlar:
    print(f"{odam['ism'].title()} {odam['familiya'].title()}. Yoshi: {2025 - int(odam['tugilgan_yili'])} ")

    if odam['tel_raqam']:
        tel_raqam = odam['tel_raqam']
    else:
        print('Telefon raqam berilmagan! ')
"""

# 3 - mashq

"""
print('3 ta sonni kattasini topamiz')

def kattasi(a, b, c):
    max = a

    if b >= max:
        max = b
    if c >= max:
        max = c
"""

# 4 - mashq
"""
def aylana(radius):
    pi = 3.14159

    aylana_detal = {
        'radius': radius,
        'diametr': radius * 2,
        'uzunlik': radius * 2 * pi,
        'yuzi': (radius**2)*pi
    }
    return aylana_detal

jami = []

while True:
    aba = int(input('Aylanani radiusini kiriting: '))
    jami.append(aylana(aba))

    javob = input('Yana davomi bormi? ha/yoq')
    if javob.lower() == 'yoq':
        break

print('Siz belgilangan aylanalar')

for a in jami:
    print(f"Radius = {a['radius']}\nDiametr = {a['diametr']}\nUzunligi = {a['uzunlik']}\nYuzi = {a['yuzi']}")
"""

# 5 - mashq
"""
def tub_topish(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub.append(n)
    
    return tub_sonlar
"""

# 6 - mashq

def fibonachi_ketmaketligi(a):
    sonlar_toplami = [0, 1]
    for n in range(2,  a):
        sonlar_toplami.append(sonlar_toplami[-1] + sonlar_toplami[-2])

    return sonlar_toplami

num = int(input('Nechta Fibonachi sonini chiqarmoqchisiz:  '))
print(fibonachi_ketmaketligi(num))