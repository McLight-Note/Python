# 2025.02.15
# Mavzu: Funksiya va royxat
# Muallif: Muhammasodiq

import math

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f" Talaba {ism.title()}ning bahosini qoying: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'olim', 'bonu']
baholar = bahola(talabalar)
print(baholar)