from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


async def webapp(message: types.Message ):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,row_width=2)

    animix = KeyboardButton('Animix', web_app=types.WebAppInfo(url = "https://animix.lol/"))
    steam = KeyboardButton('STEAM', web_app=types.WebAppInfo(url = "https://store.steampowered.com/?l=russian"))
    deepl= KeyboardButton('DeepL.translator', web_app=types.WebAppInfo(url = "https://www.deepl.com/ru/translator"))
    spotify = KeyboardButton('Spotify', web_app=types.WebAppInfo(url = "https://open.spotify.com/"))
    pinterest= KeyboardButton('Pinterest', web_app=types.WebAppInfo(url = "https://www.pinterest.com/"))

    keyboard.add(animix,steam,deepl,spotify,pinterest)

    await message.answer(text="Доступные сайты", reply_markup=keyboard)


def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(webapp,commands=['webapp'])