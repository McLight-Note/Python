# 2025.03.30
# Mavzu: Fayllar bilan ishlash
# Muallif: Muhammadsodiq

with open('pi.txt') as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = float(pi)
print(pi)
print(type(pi)) 

filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi, 'w') as fayl:
    fayl.write(ism + '\n')
    fayl.write(str(tyil) + '\n')

with open (faylnomi, 'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')

import pickle

talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
talaba2 = {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs': 1}

with open('info', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)

with open('info', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)

# Tavsia qilingan usul

with open('talaba1', 'wb') as file:
    pickle.dump(talaba1, file)