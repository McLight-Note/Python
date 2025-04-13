# 2025.04.14
# Mavzu: JSON format, Mashqlar
# Muallif: Muhammadsodiq

import json

data = {
    'model': 'Malibu',
    'rang': 'qora',
    'yil': 2020,
    'narh': 40000
}

data_json = json.dumps(data)
with open('data.json', 'w') as f:
    json.dump(data, f)
print(data_json)

filename = 'talaba.json'
with open(filename) as f:
    talaba_json = json.load(f)
print(talaba_json)

with open('talaba2.json', 'w') as f:
    json.dump(talaba_json, f)

with open('students.json') as f:
    talabalar_json = json.load(f)

for student in talabalar_json['student']:
    print(f"Name: {student['name'].title()},\nSurename: {student['lastname'].title()},\nYear: {student['year']}\n,Faculty: {student['faculty']}")

with open('api.php.json') as f:
    matn_json = json.load(f)
page_id = list(matn_json['query']['pages'].keys())[0]
title = matn_json['query']['pages'][page_id]['title']
extract = matn_json['query']['pages'][page_id]['extract']

print(f"Sarlavha: {title}")
print(f"Qisqa matn: {extract}")