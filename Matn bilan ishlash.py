# 4-dars. Matn bilan ishlash
# 20.06.2024
# Muallif: Muhammadsodiq

"""
# 1 exa

ism = "Abdulloh"
print("Mening ismim " + ism)

ism = "Ahad"
familiya = "Qayyum"
print(ism + familiya)
print(ism + ' ' + familiya)

# 2 exa

ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

# 3 exa

ism = "James"
familiya = "Bond"
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# 4 exa

print("Hello world!")
print("Hello \tworld!") # \t == tab
print("Hello \nworld!") # \n == next

# 5 exa

print(ism_sharif)
print(ism_sharif.upper())
ism_sharif = ism_sharif.upper()
print(ism_sharif)

# 6 exa

print(ism_sharif.lower()) # kichiklashtirish
print(ism_sharif.title()) # birinchi harflarni kattalashtirish
print(ism_sharif.capitalize()) # faqat boshidagi harfni kattalashtiradi

# 7 exa # bo'shliqlarni o'chirish

meva = "    olma    "
print(meva)
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")

"""

# 8 exa #INPUT

ism = input("Ismingiz nima? /n>>> ")
print("Assalomu alaykum, " + ism.title())