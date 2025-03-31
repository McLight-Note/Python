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
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = pi.replace(" ", "")

bdate = "31122000"
print(bdate in pi)

pi = float(pi)

with open(file1, 'wb') as file:
    pickle.dump(pi, file)

fayl2 = 'info'
with open(fayl2, 'w') as file:
    file.write('Adbulloh Otamirzayev\n')
    file.write('2006')

