# 2025.03.06
# Mavzu: Kalkulator
# Muallif: Muhammadsodiq

import math

def qoshish(a,b):
    return a + b

def ayrish(a,b):
    return a - b

def kopaytma(a,b):
    return a * b

def boluv(a,b):
    if b == 0:
        print('Impossible to divide to "0"')
        return None
    else:
        return a / b

while True:
    javob = input("Press '1' to add numbers;"
                   "\nPress '2' to subtract numbers;"
                   "\nPress '3' to multiply numbers;"
                   "\nPress '4' to divide numbers;"
                   "\n-------> ")

    if javob in ('1', '2', '3', '4'):
        num1 = int(input(" a: "))
        num2 = int(input(" b: "))

        if javob == '1':
            print("Result:", qoshish(num1, num2))
        elif javob == '2':
            print("Result:", ayrish(num1, num2))
        elif javob == '3':
            print("Result:", kopaytma(num1, num2))
        elif javob == '4':
            print("Result:", boluv(num1, num2))
    else:
        print("Incorrect input! Please select another option :)")

    davom = input("Do you want to continue? (yes/no): ")
    if davom.lower() != 'yes':
        break