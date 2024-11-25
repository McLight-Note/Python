# 03.11.2024
# Nesting
# Muallif: Muhammadsodiq
import math

"""ilm_fan = {
    'ism':'elon',
    'familiya':'musk',
    'tyil':1975,
    'tjoy':'amerika'}
sanat = {
    'ism':'ozodbek',
    'familiya':'nazarbekov',
    'tyil':1978,
    'tjoy':'andijon'}
internet = {
    'ism':'joe',
    'familiya':'rogan',
    'tyil':1972,
    'tjoy':'meksika'}
texnika = {
    'ism':'ali',
    'familiya':'valiyev',
    'tyil':2005,
    'tjoy':'toshkent'}
odamlar = [ilm_fan, sanat, internet, texnika]

for shaxs in odamlar:
    print(f"{shaxs['ism'].title()} {shaxs['familiya'].title()} {shaxs['tyil']} - yilda {shaxs['tjoy'].title()}da tavallud topgan.\n"
          f"{abs(shaxs['tyil'] - 2024)} yil umr ko'rgan")"""

"""ilm_fan = {
    'ism':'elon',
    'familiya':'musk',
    'tyil':1975,
    'tjoy':'amerika',
    'asarlar':['tesla','spaceX']}
sanat = {
    'ism':'ozodbek',
    'familiya':'nazarbekov',
    'tyil':1978,
    'tjoy':'andijon',
    'asarlar':['keldi bahor', 'jigi-jigi']}
internet = {
    'ism':'joe',
    'familiya':'rogan',
    'tyil':1972,
    'tjoy':'meksika',
    'asarlar':['talkto','meeting']}
texnika = {
    'ism':'ali',
    'familiya':'valiyev',
    'tyil':2005,
    'tjoy':'toshkent',
    'asarlar':['yoshligim','kelmadi hechkim']}

odamlar = [ilm_fan, sanat, internet, texnika]
for shaxs in odamlar:
    print(f"{shaxs['ism'].title()} {shaxs['familiya'].title()}ning asarlari ro'yxati:")
    for asar in shaxs['asarlar']:
        print(asar.title())"""

"""kinolar = {
    'dadam': ['terminator', 'vandam', 'hishnik'],
    'oyim': ['tangem', 'jumong'],
    'singlim1':['musiqa','hatiko'],
    'singlim2':['titanik', 'boyka']
}

for shaxs, kino in kinolar.items():
    print(f"{shaxs.title()}ning sevimli kinolari: ")
    for kin in kino:
        print(kin.title())"""

davlatlar = {
    "O'zbekiston":{'poytaxt':'toshkent',
        'hududi':448978,
        'aholisi':36000000,
        'pul birligi':"so'm"
    },
    'Rossiya':{'poytaxt':'moskva',
        'hududi': 17098246,
        'aholisi':144000000,
        'pul birligi':'rubl'
    },
    'AQSH':{'poytaxt':'vashington',
        'hududi':9631418,
        'aholisi':327000000,
        'pul birligi':'dollar'
    }
}

for davlat, ichi in davlatlar.items():
    print(f"{davlat}ning potaxti {ichi['poytaxt'].title()}\n"
          f"Hududi: {ichi['hududi']} kv.km\n"
          f"Aholisi: {ichi['aholisi']}\n"
          f"Pul birligi: {ichi['pul birligi']}\n")