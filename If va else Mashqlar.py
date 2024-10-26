# 26.10.2024
# Mavzu: If va else Mashqlar
# MUallif: Muhammadsodiq

import math

"""cars = ['toyota','mazda','hyunadi','gm','kia']

for m in cars:
    if m == 'gm':
        print(m.upper())
    else:
        print(m.title())"""
        
"""for m in cars:
    if m != 'gm':
        print(m.title())
    else:
        print(m.upper())"""

"""ism = input('Ismingiz nima ---> ')
ism = ism.lower()

if ism == 'admin':
    print('Hush kelibsiz Admin')
else:
    print(f"Hush kelibsiz {ism.title()}")"""

"""x = int(input('son yozing >>>'))
y = int(input('yana bitta >>>'))

if x == y:
    print('Sonlar teng ekan')"""

"""x = int(input('x = '))

if x < 0:
    print('Bu son manfiy ekan')
else:
    print('Bu son musbat ekan')"""

x = int(input('x = '))
if x >= 0:
    print(f'x ildizi = {math.sqrt(x)}')
else:
    print('Musbat son kiriting')