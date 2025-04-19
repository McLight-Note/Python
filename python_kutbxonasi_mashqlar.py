# 2025.04.19
# Mavzu: Python kutubxonasi
# Muallif: Muhamamdsodiq

import datetime as dt
from dateutil.relativedelta import relativedelta
import re

bugun = dt.date.today()
boshlanish_kun = 1
kelajak_farq = []

for kun in range(10, 20):
    if (bugun.day + kun) >= 31:
        kelajak_farq.append(boshlanish_kun)
        boshlanish_kun += 1
    else:
        kelajak_farq.append(bugun.day + kun)

print(kelajak_farq)

ramazon = dt.date(2026, 2, 17)
farq = ramazon-bugun
print(farq.days, 'kun')

tkun = dt.date(2002, 12, 26)
tkun_farq = relativedelta(bugun, tkun)
print(f'{tkun_farq.years} yil, {tkun_farq.months} oy, {tkun_farq.days} kun otdi')

"""telefon_raqam = input('Telefon raqam kirgizing: ')
andoza = "^998.........$"

if re.match(andoza, telefon_raqam):
    print('Qabu qilindi!')
else:
    print('Xato')
"""

matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI"
matn1 = "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
matnlar = [matn, matn1]

andoza = 'https?://[^\s]+'
a = 0

for n in matnlar:
    if re.search(andoza, n):
        print(f"{re.search(andoza, n).group()} ekan")
        a += 1
print(f"Jami {a} ta bor ekan")