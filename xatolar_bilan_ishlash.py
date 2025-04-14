# 2025.04.14
# Mavzu: Xatolar bilan ishlash
# Muallif: Muhammadsodiq

import json

# yosh = input('Yoshingizni kiriting:')
try:
    yosh = 12
except ValueError:
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2025-yosh} yilda tug'ilgansiz")

# Zero division error

x,y = 5,10

try:
    y/(x-5)
except ZeroDivisionError:
    print('0 ga bolih mumkin meas')

mevalar = ['olma', 'nok','uzum', 'anjir']
try:
    print(mevalar[7])
except IndexError:
    print(f'Bu royxatda {len(mevalar) + 1} ta meva bor halos')

user = {
    'username': 'olmazor',
    'status': 'admin',
    'email': 'ejwfibfwieonfi@gmail.com',
    'phone': '8193831313'
}

key = 'tel'
try:
    print(f'Foydalanuvchi: {user[key]}')
except KeyError:
    print('Bunday kalit mavjud emas')

filename = 'data.txt'
try:
    with open(filename) as f:
        f.read()
except FileNotFoundError:
    print(f'{filename} fayl mavjud emas!')

files = ['talaba1.json', 'talaba2.json', 'talaba3.json', 'talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f'{filename} fayl mavjud emas!')
        # pass
    else:
        print(talaba['ism'])

n = input('Butun son kiriting')
try:
    n = int(n)
    x = 20/n
except ValueError:
    print('Butun son kiritmadingiz!')
except ZeroDivisionError:
    print('Butun sonni 0 ga bolib bolmaydi')
else:
    print(f'x={x}')

while True:
    yosh = input('Yoshingizni kiriting')
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f'Siz {2025 - yosh} yilda tugilgansiz')