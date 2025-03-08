# 2025.03.04
# Mavzu: Telegram bot(Kiril lotin alifbo)
# Muallif:  Muhammadsodiq

from transliterate import to_cyrillic, to_latin
import telebot
from telebot import types

"""
bot = telebot.TeleBot("7806378935:AAFZQEAX1pJCz97Zr6w7HhSRZv7AenS5y3c", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button = types.KeyboardButton(text="Yusufjon")
    markup.add(button)

    print(message.text)

    bot.reply_to(message, "Assalomu alaykum, Hush Kelibsiz!", reply_markup=markup)


@bot.message_handler()
def send_welcome(message: types.Message):
    print(message)"""

bot = telebot.TeleBot("7806378935:AAFZQEAX1pJCz97Zr6w7HhSRZv7AenS5y3c", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    """
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        jaob = to_latin(msg)
        """
    bot.reply_to(message, javob(msg))

bot.polling()