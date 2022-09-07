#5309031470:AAEmk_RL37wjADRMNZtyC-H_S7_7feHc2fs
import telebot
from telebot import types
import sqlite3

token = '5309031470:AAEmk_RL37wjADRMNZtyC-H_S7_7feHc2fs'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

bot.polling(none_stop=True)