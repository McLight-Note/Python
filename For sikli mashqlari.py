# 24.09.2024
# For sikli misollari
# Muallif: Muhammadsodiq

import math

# 1 - masala

"""k = int(input('k = '))
n = int(input('n = '))
s = list(range(1, n + 1))

for a in s:
    print(f"{k}")"""

# 2 - masala

"""a = int(input('a = '))
b = int(input('b = '))
s = list(range(a, b + 1))

for a in s:
    print(f"{a}")
print('Shu sonlar hisoblanadi')"""

# 3 - masala

"""a = int(input('a = '))
b = int(input('b = '))
s = list(range(a, b + 1))
s1 = reversed(s)

for z in s1:
    print(z)"""

# 4 - masala

"""a = int(input('nechchi kg = '))
narx = int(input('narx = '))
s = list(range(1, a + 1))

for z in s:
    print(f"{z}kg = {z * narx}")
print('Shunaqa gaplar!:)')"""

# 5 - masala
# keyinga qoldirildi

"""a = int(input('kg = '))
b = int(input('narx = '))
s = list(range(1, a + 0.1))

for z in s:
    print(f"{z}kg = {z * b} somdan")"""

# 7 - masala

"""a = int(input('a = '))
b = int(input('b = '))
s = list(range(a, b + 1))
d = 0

for z in s:
    d = d + z
print(d)"""

# 9 - masala

"""a = int(input('a = '))
b = int(input('b = '))
s = list(range(a, b + 1))
d = 0

for z in s:
    d = d + z**2
print(d)"""

# 11 - masala

"""n = int(input('n = '))
s = list(range(n, (2 * n) + 1))
d = 0

for z in s:
    d = d + z**2
print(d)"""

# 15 - masala

"""a = int(input('a = '))
n = int(input('n = '))
s = list(range(1, n))
d = a

for z in s:
    a = a * d
print(a)"""

# 17 - masala

"""a = int(input('a = '))
n = int(input('n = '))
s = list(range(1, n + 1))
d = 1
l = a

for z in s:
    print(f"{l} ning {z} darajasi = {a}")
    d = d + a
    a = a * l
print(d)"""

# 19 - masala

"""n = int(input('n = '))
s = list(range(1, n + 1))
d = 1
for z in s:
    d = d * z
print(d)"""

# 20 - masala

"""n = int(input('n = '))
s = list(range(1, n + 1))
d = 1
f = 0

for z in s:
    d = d * z
    f = f + d
print(f"{f}")"""

# 23 - masala

"""n = int(input('n = '))
x = int(input('x = '))
s = list(range(1, n + 1))
d = 1
f = 0

for z in s:
    d = d * z
    f = f + (((-1)**d)*x**(2*d+1))/((2*d+1))
print(f)"""

# 29 - masala

"""n = int(input('n = '))
A = int(input('A = '))
B = int(input('B = '))
s = list(range(A, B + 1))
d = abs(B - A) / n

for z in s:
    A = A + d
    print(A)"""

"""# 36 - masala

n = int(input('n = '))
k = int(input('k = '))
s = list(range(1, n + 1))
d = 0

for z in s:
    d = d + math.pow(z, k)
print(d)"""

# 38 - masala

"""n = int(input('n = '))
k = int(input('k = '))
s1 = list(range(1, n + 1))
s2 = reversed(s1)
d = 0

for z in s1:
    d = d + math.pow(z, n -  z + 1)
print(d)"""