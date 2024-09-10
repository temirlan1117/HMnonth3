from aiogram import types, Dispatcher
from config import bot, dp
import random
games = ['🎰', '⚽', '🎳', '🎯', '🎲', '🏀']

async def echo_handler(message: types.Message):
    text = message.text
    if message.text.isdigit():
        await message.answer(int(message.text)**2)
    elif text=='game':
        random_game = random.choice(games)
        await bot.send_dice(chat_id=message.from_user.id, emoji=random_game)
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)