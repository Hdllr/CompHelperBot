#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

from telebot import types

API_TOKEN = '8102712098:AAHMM7f2gNI4VW20w0OeVfn3lY8_N1ElT3k'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='ТЕСТОВАЯ КНОПКА', url='https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "ТЕСТОВАЯ КНОПКА", reply_markup = markup)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("KEY КНОПКА 1")
    btn2 = types.KeyboardButton('KEY КНОПКА 2')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "ТЕСТОВЫЕ КНОПКИ", reply_markup=markup)

bot.infinity_polling()