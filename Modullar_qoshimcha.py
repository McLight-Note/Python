# 2025.02.19
# Mavzu: Modullar qo'shimcha
# Muallif: Muhammadsodiq

"""
import Modullar as aim

avto1 = aim.avto_info('gm','malibu', 'qora', 'avtomat', 2020, 30000)

from Modullar import avto_info

avto1 = avto_info('gm','malibu', 'qora', 'avtomat', 2020, 30000)

from Qiymat_qaytaruvchi_funksiya import avto_info as ainfo, info_print as iprint

from Qiymat_qaytaruvchi_funksiya import *
"""

import math

x = 400
print(math.sqrt(x))
print(math.pow(5,3))
print(math.pi)
print(math.Log2(8))
print(math.Log10(100))

import random as r

son = r.randint(0,100)
print(son)

ismlar = ['ali', 'olim', 'bunyod', 'tohir']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))
x = list(range(0,51,5))
print(x)
print(r.choice(x))

# shuffle()

x = list(range(11))
print(x)
r.shuffle(x)
print(x)