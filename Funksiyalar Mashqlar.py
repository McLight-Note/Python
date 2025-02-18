# 2025.02.12
# Mavzu: Funksiyalar Mashqlar
# Muallif: Muhammadsodiq

# 1 - mashq

def yosh_topamiz(ism, yil):
    """Ismini va yoshini qayta ishlab beramiz"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}\n"
          f"Sizning yoshingiz {2025 - yil}")
yosh_topamiz('olim', 2002)
yosh_topamiz('husan', 2006)

# 2 - mashq

def kv_kub(a):
    """Kvadrat va Kub chiqaraman"""
    print(f"{a} ni kvardati =  {a**2}\n"
        f" va kubi {a**3}")
kv_kub(5)
kv_kub(7)

# 3 - mashq

def juft_toq(a):
    """Juft yoki toqligini chiqaruchi funksiya"""
    if a%2 != 0:
        print(f"{a} soni toq son")
    else:
        print(f"{a} soni juft son")
juft_toq(15)
juft_toq(18)

# 4 - mashq

def kattasi_tanlov(a, b):
    """Bulardan kattasini chiqaruvchi dastur"""
    if a > b:
        print(f"Kattasi {a}")
    elif a < b:
        print(f"Kattasi {b}")
    else:
        print('Bular teng ekan!')
kattasi_tanlov(10, 15)
kattasi_tanlov(24, 14)
kattasi_tanlov(5, 5)

# 5 - mashq

def daraja_go(x, y):
    """x ning y darajasini chiqaradi"""
    print(f"{x**y}")
daraja_go(2,5)
daraja_go(5,3)

# 6 - mashq

def daraja_top(x, y = 2):
    """Kvadrat topamiz shekilli"""
    print(f" {x} ning {y} darajasi = {x**y} ga teng")
daraja_top(4,6)
daraja_top(3)

# 7 - mashq

def bolinish_alomatlari(x):
    """Bo'linish alomatlarini tekshiramiz"""
    z = 0
    for l in list(range(2,11)):
        if not x%l:
            print(f"{x} soni {l} ga bo'linadi")
            z += 1

    if z == 0:
        print(f' {x} - tub son')
    else:
        print(f"Bu son {z} ta songa bo'linar ekan")
bolinish_alomatlari(80)
bolinish_alomatlari(83)