# 2025.04.14
# Mavzu: Finskiyani tekshirish Mashqlar
# Muallif: Muhammadsodiq

import math

def biggest_number(a, b, c):
    return max(a, b, c)

def str_changer(matnlar):
    return [matn.capitalize() for matn in matnlar]

def even_number(numbers):
    return [number for number in numbers if number % 2 == 0]

def fibda_bormi(n):
    def mukammal_kvadrat(x):
        s = int(math.sqrt(x))
        return s * s == x
    return mukammal_kvadrat(5 * n * n + 4) or mukammal_kvadrat(5 * n * n - 4)