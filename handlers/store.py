from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class FSM_store(StatesGroup):
    name = State()
    size = State()
    category = State()
    value = State()
    photo = State()


async def start_fsm_reg(message: types.Message, ):
    await message.answer("введите название товара")
    await FSM_store.name.set()


async def name_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    size = ReplyKeyboardMarkup(resize_keyboard=True,
                               row_width=2)

    size_1 = KeyboardButton('L')
    size_2 = KeyboardButton('XL')
    size_3 = KeyboardButton('XXL')
    size_4 = KeyboardButton('XXXL')
    size.add(size_1, size_2,
             size_3, size_4)
    await message.answer('выберете размер ', reply_markup=size)
    await FSM_store.next()




async def size_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('назовите категорию',reply_markup=ReplyKeyboardRemove())
    await FSM_store.next()


async def category_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

        await message.answer('назовите стоимость')
        await FSM_store.next()


async def value_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['value'] = message.text

    await message.answer('добавьте фото')
    await FSM_store.next()


async def photo_load(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption='Ваш товар\n\n'
                                       f'Название: {data["name"]}\n'
                                       f'Размер: {data["size"]}\n'
                                       f'Категория: {data["category"]}\n'
                                       f'Стоимость: {data["value"]}\n'

                               )
    await state.finish()


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['store'])
    dp.register_message_handler(name_load, state=FSM_store.name)
    dp.register_message_handler(size_load, state=FSM_store.size)
    dp.register_message_handler(category_load, state=FSM_store.category)
    dp.register_message_handler(value_load, state=FSM_store.value)
    dp.register_message_handler(photo_load, state=FSM_store.photo,
                                content_types=['photo'])
