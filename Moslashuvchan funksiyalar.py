# 2025.02.16
# Mavzu: Moslashuvchan Funksiyalar (*args va **kwargs~ keywords)
# Muallif: Muhammadsodiq

import math
"""
def avto_info(kompaniya, model, rangi, korobka,yili, narhi = None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rangi': rangi,
        'korobka': korobka,
        'yili': yili,
        'narhi': narhi
    }
    return avto
avto1 = avto_info('Gm', 'malibu', 'qora','avtomat', 2018)
avto2 = avto_info('Hunday', 'sarti', 'qizil', 'mexanik', 2020, 23000)
avtolar = [avto1, avto2]
print('Onlayn bozordai mavzud moshinalar')
"""
def summa(*sonlar):
    """Kiritilgan barcha summani yigadigan funskiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2,3))
print(summa(1,2,3,5))
print(summa(1,2,3,6,7,3))

def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info('Gm', 'malibu', rangi='qizil', narhi=35000, yil=2020)
avto2 = avto_info('Nissan', 'aljero', rangi ='oq', narhi=35000, yil=2020)
avtolar = [avto1, avto2]
print(avtolar)