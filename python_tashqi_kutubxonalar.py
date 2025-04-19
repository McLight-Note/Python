# 2025.04.19
# Mavzu: Tashqi kutubxonalar
# Muallif: Muhammadsodiq

from googletrans import Translator
tarjimon = Translator()

matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"

tarjima = tarjimon.translate(matn_uz)
print(tarjima.origin)
print(tarjima.text)
print(tarjima.src)


tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)

matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest= 'uz')
print (tarjima_uz. text)

"""msg = "Tarjima uchun soz kiriting: "

while True:
    text = input(msg)
    if text == 'q':
        break
    else:
        tarjima = tarjimon.translate(text, src='uz', dest='en')
        print(tarjima.text)
        break
"""
"""import requests
from pprint import pprint

page = "https://kun.uz/news/main"
r = requests.get(page)
pprint(r.text)

country = 'Uzbekistan'
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])"""

import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests. get (url)
advice = r. json()[ 'slip']['advice']
print(advice)
translator = googletrans. Translator()
tarjima = translator.translate(advice, dest='uz')
print(tarjima.text)

from bs4 import BeautifulSoup

page = "https://kun.uz/news/main"
r = requests.get(page)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_='news-title')
# print(news[0].text)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
matn=""
for n in news:
    matn += n.text
"""
# kerakmas so'zlar
stopwords = ["учун","бўйича","лекин","билан","ва","ҳам","хил","йил"]
# bulutni yaratamiz
wordcloud = WordCloud(width = 1000, height = 1000, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 20).generate(matn) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.show()
"""

import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# copyright Tim Ruscia aka techwithtim
# code from https://github.com/techwithtim/OpenCV-Tutorials
