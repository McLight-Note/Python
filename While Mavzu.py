# 26.11.2024

# While tsikli mavzu

# Muallif: Muhammadsodiq


import math

"""ism = input('Ismingiz nima? >>>')
savol = f"Salom{ism}, Yoshingiz nechchida? ???"
yosh = input(savol)
yosh = int(yosh)
height = input('Boyingiz qancha? >>>')
height = float(height)"""

"""son = 1
while son <= 5:
    print(son, end = ' ')
    son += 1
print('Dastur tugadi!')

print('Kiritilgan sonni kvadratini chiqaradi!')
savol = 'Istalgan son kiriting'
savol += "(Dasturni toxtatish uchun 'exit' deb yozing):"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print("Dastur tigadi!")"""

"""print('Istalgan sonni kvadratini qaytaruvchi dastur!')
savol = input('Istalgan son kiriting')
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print('Dastur to\'xtadi!')"""

"""print('Istalgan sonni kvadratini chiqaradigan dastur!')
savol = 'Istalgan son kiriting'
savol += '(dastur tugashi uchun "exit" deb yozing)'

while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)
print('Dastur tugadi!')"""

"""sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        break
    else:
        print(f"{son} ning kvadrati {son**2} ga teng")"""

"""sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} ning kvadrati {son**2}ga teng")"""

son = 0
while son<10:
    son += 1
    if son%2 != 0: # '==' ni ham korib qoy
        continue
    else:
        print(son)