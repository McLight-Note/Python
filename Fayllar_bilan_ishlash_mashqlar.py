# 2025.03.31
# Mavzu: Faylr bilan ishlash Mashqlar
# Muallif: Muhammadsodiq

import pickle

faylname = 'mavzuga.txt'
with open(faylname, 'r') as file:
    for line in file:
        print(line)

file1 = 'pi_million_digits.txt'
with open(file1, 'r') as file:
    pi_digits = file.read() 
    if '122620' in pi_digits:
        print('Bor ekan')
    else:
        print('Yoq ekan')

with open(file1, 'r') as file:
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')

bd = "261220"
print(bd in pi)

with open(file1, 'wb') as file:
    pickle.dump(pi, file)