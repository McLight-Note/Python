# 15.07.2024
# Muallif: Muhammadsodiq
# Mavzu:+_+

"""cars = ['bmw', 'wolks-wagen', 'mercedes', 'comaro']
number = [1, 15, 64, 81, 54, 34, 72, 81]
print(sorted(cars))
print(number)
cars.sort()
number.sort()
uzunlik_cars = len(cars)
uzunlik_number = len(number)
print(sorted(cars, reverse = True))
print(sorted(number, reverse=True))
print(len(number))
print(len(cars))"""

"""sonlar = list(range(0,15))
print(sonlar, len(sonlar))
print(sorted(sonlar, reverse = True))"""

"""sonlar = list(range(21,31, 2))
sonlar2 = list(range(0, 100, 10))
print(sonlar)
print(sonlar2)"""

"""narxlar = [1500, 2750, 3245, 1340, 6420, 4250]
qimmat = max(narxlar)
arzon = min(narxlar)
jami = sum(narxlar)
print(f"Eng arzoni = {arzon}so'm\nEng qimmati = {qimmat}so'm\nJami = {jami}so'm")"""

cars = ['bmw', 'wolks-wagen', 'mercedes', 'comaro']
print(cars[0:2])
my_cars = cars[:]
cars[2] = 'volvo'
print(cars)
print(my_cars)
cars.append('GM')
print(cars)