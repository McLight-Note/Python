# Butun sonlarga oid masalalar
# 24.06.2024
# Muallif: Muhammadsodiq
# Integer section

import math

# 1 - masala
"""
l = int(input('l = '))
l = l//100
print(f'{l} metr')
"""

# 2 - masala
"""
m = int(input('m = '))
m = m//1000
print(f'{m} tonna')
"""

# 3 - masala
"""
a = a//1024
print(f'{a}kb')
"""

# 4 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = a//b
print(f'{c}ta bor')
"""
# 5 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = a//b
d = a - b * c
print(f"{c}ta bor, {d}ta qoldi")
"""

# 6 - masala
"""
a = int(input('a = '))
b = a // 10
c = a - b * 10
print(f'{b} onlik qismi\n{c} birlik qismi')
"""

# 7 - masala
"""
a = int(input('a = '))
b = a // 10
c = a - b * 10
d = b + c
print(f'Raqamlar yigindisi = {d}')
"""

# 8 - masala
"""
a = int(input('a = '))
b = a // 10
c = a - b * 10
d = c * 10 + b
print(f'orni almashdi -->> {d}')
"""

# 9 - masala
"""
a = int(input('a = '))
b = a // 100
print(b)
"""

# 10 - masala
"""
a = int(input(' a = '))
b = a // 100
c = (a - b * 100) // 10
d = (a - b * 100 - c * 10)
print(f'{d}{c}')
"""

# 11 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
s = b + c + d
print(f'{s}')
"""

# 12 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
print(f"{d}{c}{b}")
"""

# 13 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
result = int(f"{c}{d}{b}")
print(f"{c}{d}{b} va {result}")
"""

# 14 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
result = int(f"{d}{c}{b}")
print(result)
"""

# 15 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
result = int(f"{c}{b}{d}")
print(result)
"""

# 16 - masala
"""
a = int(input('a = '))
b = a // 100
c = (a - b * 100) // 10
d = a - b * 100 - c * 10
result = int(f"{b}{d}{c}")
print(f"{result}")
"""

# 17 - masala
"""
a = int(input('a = '))
b = a // 1000
c = (a - b * 1000) // 100
print(c)
"""

# 18 - masala
"""
a = int(input('a = '))
b = a // 1000
print(b)
"""

# 19 - masala
"""
n = int(input('n = '))
m = n // 60
print(m)
"""

# 20 - masala
"""
n = int(input('n = '))
s = n // 60 // 60
print(s)
"""

# 21, 22, 23 - masalalar
"""
n = int(input('n = '))
s = n // 60 // 60
m = (n - s * 60 * 60) // 60 
q = n - m * 60 - s * 60 * 60
print(f"{s}:{m}:{q}")
"""

# 24 - masala
"""
a = int(input('a = '))
k = a // 7
d = a - k * 7
print(f'{d}')

if d == 1:
    print('dushanba')
elif d == 2:
    print('seshanba')
elif d == 3:
    print('chorshanba')
elif d == 4:
    print('payshanba')
elif d == 5:
    print('Juma')
elif d == 6:
    print('shanba')
elif d == 0:
    print('yakshanba')
else:
    print('oshib ketdi')    
match d:
    case 1:
        print('dushanba')
    case 2:
        print('seshanba')
    case 3:
        print('chorshanba')
    case 4:
        print('payshanba')
    case 5:
        print('Juma')
    case 6:
        print('shanba')
    case 0:
        print('yakshanba')
    case _:
        print('Hato ketdi')
"""

# 25 - masala
"""
a = int(input('a = '))
k = a // 7
d = a - k * 7 + 4
print(f'{d}')

if d == 1:
    print('dushanba')
elif d == 2:
    print('seshanba')
elif d == 3:
    print('chorshanba')
elif d == 4:
    print('payshanba')
elif d == 5:
    print('Juma')
elif d == 6:
    print('shanba')
elif d == 0:
    print('yakshanba')
else:
    print('oshib ketdi')    
match d:
    case 1:
        print('dushanba')
    case 2:
        print('seshanba')
    case 3:
        print('chorshanba')
    case 4:
        print('payshanba')
    case 5:
        print('Juma')
    case 6:
        print('shanba')
    case 0:
        print('yakshanba')
    case _:
        print('Hato ketdi')
"""

# 26 - masala
"""
k = int(input('k = '))
d = k // 7
c = k - d * 7 + 2
print(c)
"""

# 27 - masala
"""
k = int(input('k = '))
s = k // 7
c = k - s * 7 + 1
print(c)
"""

# 28 - masala
"""
k = int(input(' k = '))
n = int(input('N = '))
s = k // n
c = k - s * n 
print(c)
"""

# 29 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
s1 = a * b
s2 = c ** 2
d = s1 // s2
l = s1 - d * s2
print(f"{d} ta sig'adi\n {l} oshib qoladi")
"""

# 30 - masala

a = int(input('a = '))
b = a // 100 + 1
print(f"{b} chi asr")
