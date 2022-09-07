# 5514122508:AAGNpi8KweNDHtH5E1yk2hAd6z-LgS_53cs
import telebot
from telebot import types
import sqlite3

token = '5514122508:AAGNpi8KweNDHtH5E1yk2hAd6z-LgS_53cs'
bot = telebot.TeleBot(token)

user = ''
phone = 0


@bot.message_handler(commands=['start'])
def start_user(message):
    """Creating a welcome message and moving on to the next message (function)"""
    global user
    user = message.text
    bot.send_message(
        message.chat.id,
        'Здравствуйте! Мы вас приветствуем в нашей компании "Рога и Копыта"! Укажите свои ФИО: ')
    bot.register_next_step_handler(message, phone)


def phone(message):
    """Getting the user's phone number and moving to the next message(function)"""
    global phone
    phone = message.text
    bot.send_message(message.from_user.id, 'Введите номер телефона (в формате +375 ХХ ХХХ ХХ ХХ): ')
    bot.register_next_step_handler(message, keys)


def keys(message):
    """Creating select buttons and creating database 'Dom_Telegram'."""

    keyboard = types.InlineKeyboardMarkup()
    key_man = types.InlineKeyboardButton(text='Маникюр', callback_data='mani')
    keyboard.add(key_man)
    key_ped = types.InlineKeyboardButton(text='Педикюр', callback_data='ped')
    keyboard.add(key_ped)
    bot.send_message(message.from_user.id, 'Выберите процедуру: ', reply_markup=keyboard)






@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):
    """Creating last message depending on selection"""
    conn = sqlite3.connect("Dom_Telegram_1.2.db")
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, us TEXT, ph VARCHAR(30), pr TEXT)''')
    conn.commit()
    if call.data == 'mani':
        bot.send_message(call.message.chat.id,
                         phone + ' Вы записаны на маникюр. В ближайшее время с вами свяжется специалист.')
        cursor.execute('''INSERT INTO book(us, ph, pr) VALUES(?, ?,'маникюр')''', (user, phone,))
        conn.commit()
    elif call.data == 'ped':
        bot.send_message(call.message.chat.id,
                         phone + ' Вы записаны на педикюр. В ближайшее время с вами свяжется специалист.')
        cursor.execute('''INSERT INTO book(us, ph, pr) VALUES(?, ?,'педикюр')''', (user, phone,))
        conn.commit()
        cursor.execute('''SELECT*FROM book''')
        p = cursor.fetchall()
        print(p)


if __name__ == '__main__':
    bot.polling(none_stop=True)
