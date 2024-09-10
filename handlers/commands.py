from config import dp,bot
from aiogram import types, Dispatcher

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='HELLO!'  )



async def send_file(message: types.Message):
    await bot.send_document(chat_id=message.from_user.id,document=open('config.py', 'rb') )




def register_commands(dp: Dispatcher):
    dp.register_message_handler(send_file, commands="file")
    dp.register_message_handler(start, commands=['start'])
