# 2025.04.01
# Mavzu: Fayllar bilan ishlash qo'shimcha mashqlar
# Muallfi: Muhammadsodiq

# 1-mashq
filename = 'user_name_txt'
filename2 = 'mavzuga.txt'
filename3 = 'file1.txt'
filename4 = 'file2.txt'

'''with open(filename, 'w') as file:
    file.write(input("Faylga biror narsa yozing"))
'''
# 2-mashq
'''
with open(filename, 'r') as file:
    print(file.read())
'''
# 3-mashq
'''
with open(filename, 'a') as file:
    file.write('\nKeyingi satr')
'''
# 4-mashq Counting Words in a File
'''
with open(filename2, 'r') as file:
    soz = 'Fayl'
    a = 0
    for line in file:
        a += line.count(soz)
    print(f"{a} ta {soz} bor ekan")
'''
# 5-mashq Copying a File
'''
with open(filename2, 'r') as file:
    with open('destination.txt', 'w') as infile:
        for line in file:
            infile.write(line)'''
# 6-mashq Removing Empty Lines from a File
'''
with open(filename2, 'r') as file:
    lines = file.readlines()

with open(filename2, 'w') as file:
    for line in lines:
        if line.strip():
            file.write(line)'''
# 7-mashq Merging Multiple Files
'''
with open(filename3, 'r') as file:
    with open('merged.txt', 'w') as infile:
        for line in file:
            infile.write(line)
        infile.write('\n')

with open(filename4, 'r') as file:
    with open('merged.txt', 'a') as infile:
        for line in file:
            infile.write(line)
'''
# 8-mashq Reading Large Files Efficiently
'''
with open('merged.txt', 'r') as file:
    a = 0
    for line in file:
        if a < 10:
            a += 1
            print(f'{a}-qator: >>> ',line)
'''
# 9-mashq Logging System

"""
from datetime import datetime

filename_log = 'log.txt'

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

log_message = f"{now} Log Entry. \n"

with open(filename_log, 'a') as file:
    file.write(log_message)

print("Log added!")
"""
# 10-mashq Checking If a File Contains a Specific Word

with open(filename2, 'r') as file:
    a = input('Qanday soz istayapsiz? Yozing >>> ')
    if a in file:
        print('Bu soz bor!')
    else:
        print('Bu soz yoq!')