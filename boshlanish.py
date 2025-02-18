# 2025.02.07
# Mavzu: While takrorlash
# Muallif: Muhammadsodiq

"""ism = input('Ismingizni kiriting---->')
savol = f"Salom, {ism.title()}. Yoshingiz nechchida ---> "
yosh = input(savol)
yosh = int(yosh)
height = input('Boyingiz nechchi --- >')
height = float(height)"""

"""son = 1
while son <= 5:
    print(son, end=' ')
    son += 1
print('Dastur tugadi')

print('Istalgan sonni kvadratini chiqaruchi dastur')
savol = 'Sonni kiriting'
savol += "dasturni toxtatish uchun 'exit' deb yozing"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print('Dastur tugadi')"""

"""print('Istalgan sonni kvadratini chiqaruchi dastur')
savol = 'Sonni kiriting'
savol += "dasturni toxtatish uchun 'exit' deb yozing: "
ishora = True
 
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print('Dastur to\'xtadi')"""

"""print('Istalgan sonni kvadratini chiqaruchi dastur')
savol = 'Sonni kiriting'
savol += "dasturni toxtatish uchun 'exit' deb yozing: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)
print("dastur tugadi")"""

"""sonlar = list(range(1,11))

for son in sonlar:
    if son == 5:
        break
    else:
        print(f"{son} ning kvadrati: {son**2} ga teng")
print('dastur tugadi')"""

"""sonlar = list(range(1,11))

for son in sonlar:
    if son == 5:
        continue
    else:
        print(f"{son} ning kvadrati: {son**2} ga teng")
print('Dastur tugadi')"""

son = 0
while son<10:
    son += 1
    if son%2 == 0:
        continue
    else:
        print(son)
print('Dastur tugadi')