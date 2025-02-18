# 2025.02.16
# Mavzu: Funksya va royxatlar
# Muallif: Muhammadsodiq

import math

# 1 - mashq
"""
def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
"""
# 2 - mashq
"""
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
"""
# 3 - mashq
"""
def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f" Talaba {ism.title()}ning bahosini qoying: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'olim', 'bonu']
baholar = bahola(talabalar)
print(baholar)
"""
# 4 - mashq
"""
def salom_ber(ism):
    print(f'Salom, {ism.title()}')
salom_ber('ali')
print(salom_ber)
"""
# 5 - mashq
"""
def square(numb):
    return numb**2
square(5)
print(square)
"""
# 6 - mashq
"""
def even(a):
    return a % 2 == 0
print(even(10))
print(even(7))
"""

# 7 - mashq
"""
def kattasi(a, b):
    return max(a, b)
print(kattasi(5,7))
print(kattasi(4,3))
"""

# 8 - mashq
"""
def takrorla(a, n):
    for l in range(0, n):
        print(a)
print(takrorla('Assalomu alaykum', 6))
print(takrorla('Muhammadsodiq', 7))
"""
# 9 - mashq

def uzunlik(lst):
    return len(lst)
print(uzunlik('Assalomu alaykum'))