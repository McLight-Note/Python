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
