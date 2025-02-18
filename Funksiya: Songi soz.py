# 2025.02.19
# Mavzu: Funksiyalar So'ngi so'z
# Muallif: Muhammadsodiq

import math

# lambda argument: ifoda
"""
uzunlik = lambda pi, r: 2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x, y: x ** y
print(kvadrat(3, 2))

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3ning kvadrati {kvadrat(3)}ga, kub {kub(3)}ga teng")

from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

def daraja2(x):
    return x*x

kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y: x+y, a, b))
print(a_plus_b)
"""
"""
import random as r

sonlar = r.sample(range(100),10)
print(sonlar)

def juftmi(x):
    return x%2 == 0

juft_sonlar = list(filter(juftmi,sonlar))
print(juft_sonlar)

juftmix = list(filter(lambda d: d%2 == 0, sonlar))
print(juftmix)
"""

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "govun", "banan" ]
harf = 'b'
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva)<=5,mevalar))
print(mevalar2)

list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
