# 2025.02.19
# Mavzu: Modullar
# Muallif: MUhammadsodiq

import math

"""def  avto_info(kompaniya, model, rang, korobka, yili, narh = None):
    avto = {'kompaniya':kompaniya,
            'model' :model,
            'rang' :rang,
            'korobka' : korobka,
            'yil': yili,
            'narh': narh}
    return avto

print('Saytimizda avtomobillarni royxatini shakillantiramiz')
avtolar = []
while True:
    print('\nQuyidagi malumotlarni kiriting', end = '')
    kompaniya = input('Kompaniya: ')
    model = input('model: ')
    rang = input('rang: ')
    korobka = input('korobka: ')
    yili = input('yili: ')
    narhi = input('Narhi: ')
    avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narhi))
    
    javob = input('Yana avtomobil qoshasizmi? (ha/yoq)')
    if javob == 'yoq':
        break
print('Salonizdagi avtolar: ')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")

def info_print(avto_info):
    Avtomobillar haqida malumotlar saqlangan lugatni konsolga chiqaruvchi funksiya
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$") """

def  avto_info(kompaniya, model, rangi, korobka, yili, narh=None):
    avto = {'kompaniya':kompaniya,
            'model' :model,
            'rang' :rangi,
            'korobka' : korobka,
            'yil': yili,
            'narh': narh}
    return avto
avto1 = avto_info('gm', 'malibu','qora','avtomat', 2018)
avto2 = avto_info('gm', 'gentra', 'oq', 'mexsnika', 2016, 15000)
avtolar = [avto1, avto2]

for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
    print(f"{avto['rang']} {avto['model']}. Nari: {avto['narh']}")