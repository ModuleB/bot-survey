
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from bot.states.admin import FSMAdmin


async def upload(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Загрузи фото")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Теперь введи название")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Введи описание")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply("Теперь укажи цену")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    # dp.register_message_handler(cancel_handler, state="*", commands=['отмена', 'cancel'])
    # dp.register_message_handler(cancel_handler, Text(equals=['отмена', 'cancel'], ignore_case=True), state="*")
    dp.register_message_handler(upload, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
