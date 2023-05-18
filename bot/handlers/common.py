from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}!\nЭто бот был создан для стать на сайте directprobi.ru\nНапишите комманду \help чтобы получить подробную информацию о возможнастях бота",
        reply_markup=types.ReplyKeyboardRemove())

async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/about - Получить анотацию к проекту",
            "/test - Первый опрос для получение первичной информации",)
    await message.answer("\n".join(text))

async def cmd_about(message: types.Message, state: FSMContext):
    await state.finish()
    text = ("Создатель бота: ",
            "Роман",)
    await message.answer("\n".join(text))

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("ok", reply_markup=types.ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start", "старт"], state="*")
    dp.register_message_handler(cmd_help, commands=['help', "помощь"], state="*")
    dp.register_message_handler(cmd_cancel, commands=["cancel", "отмена"], state="*")
    dp.register_message_handler(cmd_about, commands=["about", "info", "инфо", "информация"], state="*")
    dp.register_message_handler(cmd_cancel, Text(equals=["отмена", "отменить", "cancel"], ignore_case=True), state="*")
