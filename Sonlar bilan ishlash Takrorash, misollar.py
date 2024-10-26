# 20.09.2024
# Sonlar bilan ishlash: Takrorlash, misollar
# Muallif: Muhammadsodiq

import math

# 1 - misol
"""
a = int(input('a = '))
b = int(input('b = '))
c = a + b

print(c)
"""

# 2 - misol

"""a = int(input('a = '))
c = a / 2

print(a)"""

# 3 - misol

"""a = int(input('a = '))
b = int(input('b = '))
c = a // b
d = a - c * b
print(f"Javob: {c}, qoldiq {d}")"""

# 4 - misol

"""a = int(input('a = '))
b = int(input('b = '))
c = math.pow(a, b)

print(c)"""

# 5 - misol

"""gap = input('Nimadur deng')

print(len(gap))"""

# 6 - misol

"""r = int(input('r = '))
pi = 3.14159
S = pi * r**2
print(f'Yuzi = {S}\nDiametr = {r * 2}')"""

# 7 - misol

"""a = int(input('a = '))
b = int(input('b = '))
c = a / 100 * b
print(f"{c}")"""

# Kimsanov. Q ... Masalalar
# boshqa kitobdan masalalar

# 1 - misol

"""a = int(input('a = '))
b = a * 100
print(f"{b}")"""

# 2 - misol

"""a = int(input('a = '))
b = a * 1000
print(b)"""

# 16 - masala

"""a = int(input('a = '))
b = a // 100
c = (a -  b * 100) // 10
d = a - b * 100 - c * 10
s = c * 100 + d * 10 + b
print(s)"""

# 23 - masala

"""a = int(input('a = '))
soat = a // 3600
minut = (a - soat * 3600) // 60
sekund = a - soat * 3600 - minut * 60
print(f"{soat} : {minut} : {sekund}")"""

# 29 - masala

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
A = a // c
B = b // c
s1 = a * b
s2 = A * B
s3 = s1 - s2
soni = A * B

print(f"soni - {soni}\noshgan yuza - {s3}")