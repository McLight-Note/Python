# 27.10.2024
# Dictionary (Lug'at)
# Muallif: Muhammadsodiq

import math

"""otam = {
    'ismi': 'Sherzodbek',
    't_yili': 1978,
    'shahri': 'Maslahat'
}

print(f" Otmaning ismi - {otam['ismi'].title()}\n {otam['t_yili']} - yilda tugilan\n {otam['shahri']} da tug'ilgan")"""

"""taomlar = {
    'otam': 'palov',
    'onam': 'qozonkabob',
    'ukam': 'siltama',
    'singlim': 'shashlik',
    'akam': 'kabob'
}

print(f"Otamning sevimli taomi - {taomlar['otam']}\n Onamning sevimli taomi - {taomlar['onam']}\n Ukamning sevimli taomi - {taomlar['ukam']}\n Singlimning sevimli taomi - {taomlar['singlim']}\n Akamning sevimli taomi - {taomlar['akam']}")"""

"""lugat = {
    'integer': 'Butun son', 'float': 'Aniq son', 'string': 'Matn',
    'for': 'Takrorlash', 'else': 'yoki', 'if': 'agar', 'elif': 'va agar',
    'in': 'da', 'not': 'emas'
}

print(lugat)"""

lugat = {
    'integer': 'Butun son', 'float': 'Aniq son', 'string': 'Matn',
    'for': 'Takrorlash', 'else': 'yoki', 'if': 'agar', 'elif': 'va agar',
    'in': 'da', 'not': 'emas'
}
x = input('Biror soz kiriting: ')

if x in lugat:
    print(f"{lugat[f'{x}']}")
else:
    print('Bizda bunday soz mavjud emas!')