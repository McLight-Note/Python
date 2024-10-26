import math
from math import sqrt

""""
a = int(input("Kvadrat tomonini yozing >>> "))

b = 4*a
print(math.sqrt(16))
print("Perimetri = " , b , " ga teng")
print(f"peprimetri {b} ga teng. a={a}")
abs = print

abs(32)
"""
# 1 - masala
""""
a = int(input("Kvadrat tomonini kiriting /n >>>"))
b = 4 * a
print(f"Uning perimetri {b} ga teng")
"""

# 2 - masala
"""
a = int(input('>>>'))
s = a ** 2
print(f"S = {s}")
"""

# 3 - masala
"""
a = int(input("a = "))
b = int(input("b = "))
s = a * b
p = 2 * (a + b)
print(f'S = {s} \nP = {p}')
"""

# 4 -masala
"""
d = int(input("Son kiriting - >> "))
pi = 3.14159
l = pi * d
print(f"Aylana uzunligi {l} ga teng")
"""

# 5 - masala
"""
a = int(input("Kubning yon tomoni -->> "))
V = a**3
S = 6 * a**2
print(f"Hajmi {V} ga teng. Sirti {S} ga teng")
"""

# 6 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
v = a * b * c
s = 2 * ( a * b + b * c+ a * c)
print(f" Uning hajmi {v} ga teng. Sirti {s} ga teng")
"""

# 7 - masala
"""
r = int(input('doiraning radiusi - > '))
pi = 3.14159
l = 2 * pi * r
s = pi * r**2
print(f"Uning uzunligi {l} ga teng. Yuzi {s} ga teng")
"""

# 8 - masala
"""
a = int(input(' a = '))
b = int(input(' b = '))
c = (a + b) / 2
print(f" {a} va {b} ning o'rta arimetigi {c} ga teng")
"""

# 9 - masala
"""
a = int(input(' a = '))
b = int(input(' b = '))
c = math.sqrt(a * b)
print(f"Ularning o'rta geometrigi {c} ga teng")
"""

# 10 - masala
"""
a = int(input(' a = '))
b = int(input(' b = '))
c = a + b
d = a * b
a = a**2
b = b**2
print(f"Yig'indi = {c} \nKo'paytma = {d} \nKvadrat a = {a} \nKvadrat b = {b}")
"""

# 11 - masala
"""
b = int(input('b = '))
c = math.sqrt(a**2 + b**2)
p = a + b + c
print(f"Gipoptenuza = {c} \nPerimetri = {p}")
"""

# 12 - masala 16 - masalada ishlandi

# 13 - masala
"""
r1 = int(input('r1 = '))
r2 = int(input('r2 = '))
pi = 3.14159
s1 = pi * r1**2
s2 = pi * r2**2
s3 = s1 - s2
print(f"Yuza1 = {s1} \nYuza2 = {s2}\nUlarning ayirmasi = {s3}")
"""

# 14 - masala
"""
l = int(input(' L = '))
pi = 3.14159
r = l / (2 * pi)
s = pi * r**2
print(f'Yuza = {s}\nRadius = {r}')
"""

# 15 - masala
"""
s = int(input(' s = '))
pi = 3.14159
r = math.sqrt(s / pi)
d = 2 * r
print(f'R = {r}\nD = {d}')
"""

# 16 - masala
"""
a = int(input(' a = '))
b = int(input(' b = '))
c = abs(a - b)
print(f" Oraliq = {c}")
"""

# 17 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
ac = abs(a - c)
bc = abs(b - c)
l = ac + bc
print(f"AC = {ac}\nBC = {bc}\nUlarning umumiy uzuligi = {l}")
"""

# 18 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
ac = abs(a - c)
bc = abs(b - c)
k = ac * bc
print(f"AC = {ac}\nBC = {bc}\n Ko'paytma = {k}")
"""

# 19 - masala
"""
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
a = abs(x1 - x2)
b = abs(y1 - y2)
p = 2 * (a + b)
s = a * b
print(f"Perimeti = {p}\nYuzi = {s}")
"""

# 20 - masala
"""
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
m = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f"Masofa = {m}")
"""

# 21 - masala
"""
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))
a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Yuzi = {s}\nPerimetri = {p * 2}")
"""

# 22 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = a
a = b
b = c
print(f"a = {a}\nb = {b}")
"""

# 23 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = c
c = b
b = a
a = d
print(f"a = {a}\nb = {b}\nc = {c}")
"""

# 24 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = a
a = b
b = c
c = d
print(f'a = {a}\n b = {b}\n c = {c}')
"""

# 25 - masala
"""
x = int(input('x = '))
y = 3 * x**5 - 6 * x**2 - 7
print(f'y = {y}')
"""

# 26 - masala
"""
x = int(input('x = '))
y = 4 * (x- 3)**5 - 7 * (x - 3)**3 + 2
print(f'y = {y}')
"""

# 27 - masala       24.06.2024
"""
x = int(input('x = '))
y = int(input('y = '))
x = x**y
print(f"{y} daraja = {x}")
"""

# 28 - masala 27 bilan bir hil

# 29 - masala
"""
a = int(input('a = '))
r = 58.17
a = a / r
print(a)
"""

# 30 - masala
"""
r = int(input('r = '))
a = 58.17 * r
print(a)
"""

# 31 - masala
"""
tf = int(input('Tf = '))
tc = (tf - 32) * 5 / 9
print(f'Tc = {tc}')
"""

# 32 - masala
"""
tc = int(input('Tc = '))
tf = tc * 9 / 5 + 32
print(tf)
"""

# 33 - masala
"""
x = int(input('x = '))
a = int(input('a = '))
y = int(input('y = '))
d = a / x
b = y * d
print(f'1kg = {d}\n{y}kg = {b}')
"""

# 34 - masala
"""
x = int(input('x = '))
a = int(input('a = '))
y = int(input('y = '))
b = int(input('b = '))
s1 = a / x
s2 = b / y
su = abs(s1 - s2)
print(f" 1kg shokolad {s1}\n 1kg konfet {s2}\n Farqi = {su}")
"""

# 35 - masala
"""
v = int(input('v = '))
u = int(input('u = '))
t1 = int(input('T1 = '))
t2 = int(input('T2 = '))
a = (v + u) * t1
b = abs(v - u) * t2
s = a + b
print(f"Jami {s}km yurgan")
"""

# 36 - masala
"""
v1 = int(input('v1 = '))
v2 = int(input('v2 = '))
s = int(input('s = '))
t = int(input('t = '))
a = v1 * t
b = v2 * t
su = a + b + s
print(f"Ular orasidagi masofa {su}")
"""

# 37 - masala
"""
v1 = int(input('v1 = '))
v2 = int(input('v2 = '))
s = int(input('s = '))
t = int(input('t = '))
a = v1 * t
b = v2 * t
su = abs(s - a - b)
print(su)
"""

# 38 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
x = -b/a
print(x)
"""

# 39 - masala
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = b**2 - 4 * a * c
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)
print(f" x1 = {x1}\n x2 = {x2}")
"""

# 40 - masala

a1 = int(input('a1 = '))
b1 = int(input('b1 = '))
c1 = int(input('c1 = '))
a2 = int(input('a2 = '))
b2 = int(input('b2 = '))
c2 = int(input('c2 = '))
d = (a1 * b2 - a2 * b1)
x = (c1 * b2 - b1 * c2) / d
y = (a1 * c2 - a2 * c1) / d
print(f"x = {x}\n y = {y}")
