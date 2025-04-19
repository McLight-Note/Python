# 2025.04.19
# Mavzu: Python kutubxonalari
# Muallif: Muhammadsodiq

import datetime as dt

hozir = dt.datetime.now()
print(hozir, hozir.hour, hozir.second, hozir.minute)

bugun = dt.date.today()
print(f'Bugungi sana {bugun}')

ertaga = dt.date(2025, 4,20)
print(ertaga)

hozir1 = dt.datetime.now()
vaqtHozir = hozir1.time()
vaqtKeyin = dt.time(12, 10, 25)
print(vaqtHozir, vaqtKeyin)

ramazon = dt.date(2026, 2, 17)
farq = ramazon - bugun
print(f'Ramazonga {farq} kunq oldi')

futbol = dt.datetime(2025, 4, 23, 23, 10, 00)
farq1 = futbol - hozir
sekundlar = farq1.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbolga {farq1.days} kunu {soatlar} soat qodi")

import math

PI = math.pi
print(f"PI ning qiymati: {PI}")

E = math.e
print(f"e ning qiymati: {E}")

math.sin(math.pi/2)
math.cos(0)
math.tan(PI)
print(math.degrees(math.pi/2))
print(math.radians(90))

print(f" {math.log(5) + math.log10(100)}")

x = 4.6
print(math.ceil(x))
print(math.floor(x))

print(math.sqrt(81))

print(math.pow(x,3), math.pow(x, 5))


from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(bemor)
pprint(bemor)


# import requests

# r = requests.get('https://api.github.com')
# print(r)
# pprint(r)

import re
from uzwords import words

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)

print(matches)

matn = """18-aprel kuni O‘zbekistonda sodir bo‘lgan muhim voqealar dayjesti
📝 Harvard Growth Lab: 5 yil ichida O‘zbekiston iqtisodiy murakkablik reytingida 25 pog‘onaga ko‘tarildi
🔴 Shavkat Mirziyoyev dunyodagi iqtisodiy va savdo cheklovlarining O‘zbekistonga ta’siri haqida gapirdi
❗️ 1-iyuldan birorta tovar eksportiga cheklov bo‘lmasligi e’lon qilindi
✈️ Urganch aeroportini modernizatsiya qilish va boshqarish bo‘yicha o‘tkazilgan tender g‘olibi aniqlandi
🔍Shakarga aksiz to‘lovi bekor qilinadi. Quruq sut importiga qo‘yilgan cheklovlar ham olib tashlanadi 
📌 Xavf darajasi yuqori bo‘lgan 7 ta tovar guruhidagi mahsulotlarni davlat ro‘yxatidan o‘tkazish amaliyoti bekor qilinadi
Batafsil 👉 https://uzreport.news/society/18-aprel-kuni-o-zbekistonda-sodir-bo-lgan-muhim-voqealar-dayjesti
rtmkonferensiva2021@mail.ru
"""

andoza1 = '[ -~]'
email = re.findall(andoza1, matn)
# print(email)

# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi

andoza2 = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza2, password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")

