# 2025.05.27
# Mavzu: Training the python
# Muallif: Muhammadsodiq

import math

"""
def frequeancy_counter(list):
    freq = {}
    for a in list:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
    return freq

numbers = [1,1,1,2,2,2,2,3,3,3,3,3]
print(frequeancy_counter(numbers))

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 10
print(f"Fibonacci ketma-ketligi ({n} ta son):")
print(fibonacci(n))
"""
"""
a = int(input('>>'))
for n in range(0, a+1):
    print(n)
"""
'''
a, b = 7, 8
print(sum([a, b]))

print(a,b)
z = a
a = b
b = z
print(a, b)
'''
numbers = []
while True:
    numbers.append(input('>>>'))
    if 'stop' in numbers:
        break