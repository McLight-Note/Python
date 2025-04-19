from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

print(fuzz.ratio('salom', 'assalom'))
print(fuzz.ratio('salom', 'salim'))

text = "салом"
matches = process.extract(text, words, limit=3)
print (matches)

text = "талба"
match = process.extractOne(text, words)
print(match)
