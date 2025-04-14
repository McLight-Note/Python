# 2025.04.14
# Mavzu: Funksiyani tekshirish
# Muallif: Muhammadsodiq

def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f'{ism} {otasi} {familiya}'.title()
    else:
        return f'{ism} {familiya}'.title()