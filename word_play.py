# 2025.02.23
# Mavzu: So'z topish oyini
# Muallif: Muhammadsodiq

from uzwords import words
import random

def get_word():
    word = random.choice(words)
    while "-" in words or " " in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word)

    
    user_letters = ""
    print(f"Men {len(word)} honali so'z oyladim. Topa olasizmi?")
    result = "-----"

    while len(word_letters) > 0 and result != word:
        result = display(user_letters, word)
        print(result)
        if len(user_letters) > 0:
            print(f" Shu vaqtgacha chiqargan harflaringiz: {user_letters}")
        
        letter = input(f"Harfni kiriting:").upper()
        if letter in user_letters:
            print('Bu harfni oldin kiritgansi. Boshqa harf kiriting')
            continue
        elif letter in word:
            word_letters.remove(letter)
        else:
            print("Bunday harf yo'q")
        user_letters += letter

    print(f"Tabriklayman! Siz {word} so'zini {len(user_letters)} ta urinishda topdingiz")  



if __name__ == "__main__":
    play()