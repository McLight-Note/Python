# 2025.02.16
# Mavzu: Moslashuvchan funksiyalar, args & kwargs
# Muallif: Muhammadsodiq

import math

# 1 - mashq
"""
def kopaytma(*sonlar):
    summa = 1
    for son in sonlar:
        summa *= son
    return summa
print(kopaytma(1,2,3,4,5))
"""

# 2 - mashq

def talaba_malumotlari(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism.title()
    malumotlar['familiya'] = familiya.title()
    return malumotlar
print(talaba_malumotlari('shoxrux', 'jorayev', kurs = 3, yoshi = 22))
