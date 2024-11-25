# 26.11.2024

# While tsiksli Mashqlar

# Muallif: Muhammadsodiq

import math

# 1 - mashq

"""savol = input('Yoqtirgan kitobingizni kiriting ')
savol += " (dastur tugashi uchun 'stop' deb yozing) "
kitoblar = []

while True:
    kitob = input(savol)
    if kitob == 'stop':
        break
    kitoblar.append(kitob)
print(f"Rahmat, mana shu kitoblar sizniki >> {kitoblar}")"""

# 2 - mashq

"""savol = input("Yoshingiz nechchida? ")
savol += ' (dastur tugashi uchun "exit" yoki "quit" deb yozing): '
ishora = True;

while ishora:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        ishora = False
    yosh = int(qiymat)
    
    if yosh <= 7:
        print('Siz uchun bilet narxi 2000 so\'m')
    elif yosh <= 18:
        print('Siz uchun bilet narxi 3000 so\'m')
    elif yosh <= 65:
        print('Siz uchun bilet narxi 10000 so\'m')
    else:
        print("Sizga kirish bepul")
print('Rahmat!')"""

# 3 - mashq

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if qiymat == 'exit' or qiymat == 'quit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Rahmat!")