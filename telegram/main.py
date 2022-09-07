import logging
from aiogram import Bot, executor, types, Dispatcher
from db import Database

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5309031470:AAEmk_RL37wjADRMNZtyC-H_S7_7feHc2fs")
dp = Dispatcher(bot)
db = Database('database.db')
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Hello!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)