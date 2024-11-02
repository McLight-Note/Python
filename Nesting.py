# 01.11.2024
# Nesting
# Muallif: Muhammadsodiq

import math

car0 = {
    'model': 'nexia',
    'yil': 2017,
    'rangi': 'oq',
    'narxi': 15000,
    'korobka': 'mehanik'
}

car1 = {
    'model': 'matiz',
    'yil': 2013,
    'rangi': 'qora',
    'narxi': 7000,
    'korobka': 'mehanik'
}

car2 = {
    'model': 'honda',
    'yil': 2024,
    'rangi': 'pushti',
    'narxi': 18000,
    'korobka': 'avtomat'
}

print(f"{car0['model'].title()}, "
      f"{car0['narxi']}$, {car0['rangi']} rang, "
      f"{car0['korobka']}")

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
      f"{car['narxi']}$, {car['rangi']} rang, "
      f"{car['korobka']}")

print(cars[0]['model'])
print(f"{cars[0]['rangi'].title()} {cars[0]['model'].lower()}")

malibus = []
for n in range(10):
    new_car = {
        'model': 'malibu',
        'yil': 2024,
        'rangi': 'oq',
        'narxi': 22000,
        'korobka': 'avto'
    }
    malibus.append(new_car)

for malibu in malibus:
    print(malibu)

for malibu in malibus[:3]:
    malibu['rangi']='qizil'

for malibu in malibus[3:6]:
    malibu['rangi'] = 'qora'

for malibu in malibus[6:10]:
    malibu['rangi'] = 'qora'
    malibu['korobka'] = 'mexanik'

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narxi'] = 40000
    else:
        malibu['narxi'] = 34000

for malibu in malibus:
    print(malibu)

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dastrulash tillarni biladi")
    for til in tillar:
        print(f"{til.upper()}", end=' ')

hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyil':1995,
            'tillar': ['c++','python']},
    'vali':{'familiya':'aliyev',
            'tyil':2000,
            'tillar':['c#','sql']},
    'hasan':{'familiya':'husanov',
             'tyil':2005,
             'tillar':['html','css','js']},
    'husan':{'familiya':'hasanov',
             'tyil':2007,
             'tillar':['php','python']}
             }
for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']} - yilda tug'ilgan. \n"
          "Quyidagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(til.upper())