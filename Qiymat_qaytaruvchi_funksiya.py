# 2025.02.15
# Mavzu: Qiymat qaytaruchi funksiya (Mavzu)
# Muallif: Muhammadsodiq

import math

def toliq_ism_yasash(ism, familiya):
    """To'liq ism yaratuvchi funksisya"""
    toliq_ism = f"{ism} {familiya}"
    print(toliq_ism)
toliq_ism_yasash('hasan', 'olimov')
talaba1 = toliq_ism_yasash('obid', 'begzodov')


def toliq_ism_yasash2(ism, familiya, otasining_ismi = ''):
    """Otasining ismini ham qoshadigan funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familiya.title()}"
    else:
        toliq_ism = f"{ism.title()} {familiya.title()}"
    return toliq_ism.title()

talaba2 = toliq_ism_yasash2('shaxzod', 'burxonov')
talaba3 = toliq_ism_yasash2('shoxrux', 'ketmonov', 'otamirzaevich')

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

def oraliq(min,max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,10))
print(oraliq(10,20))

def  avto_info(kompaniya, model, rangi, korobka, yili, narh = None):
    avto = {'kompaniya':kompaniya,
            'model' :model,
            'rang' :rangi,
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
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    javob = input('Yana avtomobil qoshasizmi? (ha/yoq)')
    if javob == 'no':
        break
print('Salonizdagi avtolar: ')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")