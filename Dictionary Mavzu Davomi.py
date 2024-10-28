# 28.10.2024
# Dictionary davomi
# Muallif: Muhammadsodiq

import math

"""talaba_0 = {
    'ism': 'Bobur',
    'familiya': 'Shamvsieyv',
    'yosh': '21',
    't_yil': '2002'
}
print(talaba_0.items())

for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}\n")"""

"""telefonlar = {
    'ali': 'iphone',
    'boba': 'nokia',
    'vali': 'google'
}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni - {q}")"""

"""mahsulotlar = {
    'olma': 10000,
    'nok': 5000,
    'behi': 15000,
    'uzum': 7000
}

print(mahsulotlar.keys())

for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())"""

mahsulotlar = {
    'olma': 10000,
    'nok': 5000,
    'behi': 15000,
    'uzum': 7000
                }
bozorlik = ['anor', 'uzum', 'non', 'baliq']
"""for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f" Iltimos, do'koningizga {buyum} ham olib keling")

for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())"""

"""telefonlar = {
    'ali': 'iphone',
    'boba': 'nokia',
    'vali': 'google',
    'buva': 'iphone',
    'gani': 'mi note',
    'akrom': 'google'
}

print(telefonlar.values())

for tel in telefonlar.values():
    print(tel.title())

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi')
for tel in set(telefonlar.values()):
    print(tel.title())"""

toys = {'ball', 'car', 'lamp', 'ball'}
print(toys)