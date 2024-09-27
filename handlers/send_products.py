import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn
def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT p.product_id, p.name_product, p.size, p.price, p.photo,
           pd.category, pd.info_product,
           cp.collection_products
    FROM products p
    INNER JOIN product_detail pd ON p.product_id = pd.productid
    INNER JOIN collection_products cp ON p.product_id = cp.product_id
    """).fetchall()
    conn.close()
    return products
async def start_sending_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    show_all_products = InlineKeyboardButton(text="Посмотреть",
                                             callback_data="show_all")
    keyboard.add(show_all_products)
    await message.answer(text='Нажмите на кнопку, чтобы посмотреть товары:',
                         reply_markup=keyboard)
async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()
    if products:
        for product in products:
            caption = (f"Артикул - {product['product_id']}\n"
                       f"Название товара - {product['name_product']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"Коллекция - {product['collection_products']}\n"
                       f"категория - {product['category']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']} сом\n")
            await callback_query.message.answer_photo(photo=product['photo'],
                                                      caption=caption)
    else:
        await callback_query.message.answer("Товары не найдены!")
def register_send_products_handler(dp: Dispatcher):
    dp.register_message_handler(start_sending_products, commands=['products'])
    dp.register_callback_query_handler(send_all_products, Text(equals='show_all'))