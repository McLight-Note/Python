# 27.10.2024
# 14-dars Dictionary (Lug'at)
# Muallif: MUhammadsodiq

import math

"""car_0 = {'model': 'Ferrari', 'rang': 'qizil'}
print(car_0['model'])
print(car_0['rang'])"""

"""en_uz = {'apple': 'olma', 'apricot': 'orik', 'banana': 'banan'}
mevalar = {'olma': 10000, 'orik': 8000, 'kartoshka': 5000}
print(en_uz)
print(en_uz['apple'])
print(f"Olma narhi {mevalar['olma']} so'm")"""

"""talaba_0 = {'ism': 'murod olimov', 'yosh':24, 't_yil': 2000}
print(f"{talaba_0['ism'].title()} \n {talaba_0['t_yil']} - yilda tug'ilgan \n {talaba_0['yosh']} yoshda")

talaba_0['kurs'] = 4
talaba_0['kasb'] = 'Duradgor'
talaba_0['fakultet'] = 'Informatika'
print(talaba_0)

del talaba_0['yosh']
print(talaba_0)

del en_uz['banana']
print(en_uz)"""

telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy',
    'olim': 'nokia',
    'anvar': ' mi 5',
    'orif': 'iphone 17 Pro Max'
}

phone = telefonlar.get('ali', 'Bunday ism mavjud emas')
print(phone)

