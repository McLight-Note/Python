# 2025.02.22
# Mavzu: So'z topish o'yini
# Muallif: Muhammadsodiq

""" # Meni yechimim
import math
import random

print('Son oylayman siz topasiz')
a1 = 0
oylangan_son = random.randint(0, 10)
notogri1 = True

def son_top(x):
    a1 = 0
    while True:
        if x == oylangan_son:
            a1 = a1 + 1
            print(f"Siz {a1} urunishda topdingiz")
            notogri1 = False
            break
        elif x >= oylangan_son:
            print(f'Men oylagan son {x} dan kichkina')
            a1 = a1 + 1
            break
        elif x <= oylangan_son:
            a1 = a1 + 1
            print(f"Men o'ylagan son {x} dan katta")
            break

while notogri1 == True:
    qiymat = son_top(int(input('Oylagan soningizni yozing: ')))
"""

import random

def sontop(x = 10):
    tasodifiy = random.randint(1, x)
    print(f" Men 1 dan {x} gacha son oyladim topa olasizmi? ")
    taxminlar = 0
    while True:
        taxmin = int(input(" >>> "))
        taxminlar += 1
        if taxmin < tasodifiy:
            print("xato. Tasodifiy son bundan kattaroq")
        elif taxmin > tasodifiy:
            print("Xato. Tasodifiy son bundan kichikroq")
        else:
            break
    print(f'Tabriklaymiz, siz {taxminlar} bilan topdingiz')
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x}gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} qadamda topdim!")
    return taxminlar

def play(x = 10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user > taxminlar_pc:
            print(" Men yutdim! ")
        elif taxminlar_user < taxminlar_pc:
            print('Siz yutdingiz')
        else:
            print('Durrang')
        
        yana = int(input('Yana oynaysizmi? ha(1)/yoq(0):'))
        