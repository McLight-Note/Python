# 2025.04.13
# Mavzu: JSON format
# Muallif: MUhammadsodiq

import json

x = 10
x_json = json.dumps(x)
print(type(x_json))

y = 5.5
y_json = json.dumps(y)
print(y_json)

m = True
m_json = json.dumps(m)
print(m_json)

sonlar = (12, 45, 21, 66)
sonlar_json = json.dumps(sonlar, indent=3)
print(sonlar_json)

bemor = {
    'ism': 'Alijon Vaolev',
    'yosh': 30,
    'oila': True,
    'farzanlar': ('Ahmad', 'Bonu'),
    'allergiya': None,
    'dorilar': [
        {'nomi': 'Analgin', 'miqdori': 0.5},
        {'nomi': 'Panadol', 'miqdori': 1.2}
    ]
}

bemor_json = json.dumps(bemor, indent = 3)
print(bemor_json)

with open('sonlar.json', 'w') as f:
    json.dump(sonlar, f)

bemor2 = json.loads(bemor_json)
print(bemor2)

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)