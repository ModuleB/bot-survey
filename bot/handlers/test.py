import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, Message
from aiogram import Dispatcher

from bot.states.test import FSMTest
from create.container import user_service
from create.container import question_service
from create.create_data import create_data
from utils.print_color import print_green, print_red
from config.config import config
from bot.validators.user import full_name_verification, age_verification, email_verification, phone_verification, \
    city_verification

# Получаем вопросы и бд
questions = question_service.get_questions()

if not questions:
    create_data()
    questions = question_service.get_questions()


async def test(message: Message, state: FSMContext):
    id = message.from_user.id
    question = questions["Q1"]
    if user_service.is_already_passed(id):
        await message.answer(question, reply_markup=ReplyKeyboardRemove())
        await FSMTest.Q2.set()
    else:
        await message.answer(text="Вы уже проходили тест")
        await state.finish()


async def q2(message: Message, state: FSMContext):
    full_name = message.text
    if not full_name_verification(full_name):
        await message.answer("Пожалуйста, напишите реальное ФИО,\nиспользуя только русские буквы",  reply_markup=ReplyKeyboardRemove())
        return
    question = questions["Q2"]
    await state.update_data(full_name=full_name.title())
    await message.answer(question, reply_markup=ReplyKeyboardRemove())
    await FSMTest.next()


async def q3(message: Message, state: FSMContext):
    age = message.text
    if not age_verification(age):
        await message.answer("Пожалуйста, напишите ваш реальный возраст,\nиспользуя только цифры",  reply_markup=ReplyKeyboardRemove())
        return
    question = questions["Q3"]
    await state.update_data(age=int(age))
    await message.answer(question, reply_markup=ReplyKeyboardRemove())
    await FSMTest.next()


async def q4(message: Message, state: FSMContext):
    city = message.text
    if not city_verification(city):
        await message.answer("Пожалуйста, напишите реальный город,\nиспользуя только русские буквы",  reply_markup=ReplyKeyboardRemove())
        return
    question = questions["Q4"]
    await state.update_data(city=city.title())
    await message.answer(question, reply_markup=ReplyKeyboardRemove())
    await FSMTest.next()


async def q5(message: Message, state: FSMContext):
    email = message.text
    if not email_verification(email):
        await message.answer("Пожалуйста, введите реальный email адрес",  reply_markup=ReplyKeyboardRemove())
        return
    question = questions["Q5"]
    await state.update_data(email=email.lower())
    await message.answer(question, reply_markup=ReplyKeyboardRemove())
    await FSMTest.next()


async def q100(message: Message, state: FSMContext):
    phone = message.text
    if not phone_verification(phone):
        await message.answer("Пожалуйста, введите реальный номер мобильного телефона, начиная с 7\n(всего 11 цифр)",  reply_markup=ReplyKeyboardRemove())
        return
    await state.update_data(phone=int(phone))
    await state.update_data(tg_id=message.from_user.id)
    await state.update_data(tg_username=message.from_user.username)
    await state.update_data(date=datetime.datetime.now())
    data = await state.get_data()
    await message.answer(text="Ответы записаны", reply_markup=ReplyKeyboardRemove())
    await state.finish()

    # Тема письма
    subject = f'ID {data["tg_id"]}'

    # Текст письма
    message = f"Date: {str(data['date']).split('.')[0]}\n" \
              f"Id: {data['tg_id']}\n" \
              f"Username: {data['tg_username']}\n" \
              f"Full name: {data['full_name']}\n" \
              f"Age: {data['age']}\n" \
              f"City: {data['city']}\n" \
              f"Email: {data['email']}\n" \
              f"Phone: {data['phone']}\n"

    # Уведомление в TG
    if config.TG_NOTIFICATIONS_ENABLE:
        try:
            await bot.send_message(config.ID_FOR_NOTIFICATIONS, text=message)
            print_green(f"Id {data['tg_id']} telegram notification sent")
        except Exception as e:
            print_red("Не могу отправить уведомление в тг")
            print_red(e)

    # Уведомление по email
    user_service.send_email(message, subject)

    # Сохранение в DB
    user_service.save_data(data)




# Регистрируем хендлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(test, commands=['test'], state=None)
    dp.register_message_handler(q2, state=FSMTest.Q2)
    dp.register_message_handler(q3, state=FSMTest.Q3)
    dp.register_message_handler(q4, state=FSMTest.Q4)
    dp.register_message_handler(q5, state=FSMTest.Q5)
    dp.register_message_handler(q100, state=FSMTest.Q100)

    # сборка сообщения
    # text = []
    # for i in data:
    #     text.append(f'{data[i]}\n')
    # text='\n'.join(text)

# обработка ответа с клавиатурой

#     в посыле сообщений так...
# await message.answer(f'{question["question"]}',
#                      reply_markup=q2_keyboard())

# @dp.callback_query_handler(state=FSMTest.Q3)
# async def q3(call: Message, state: FSMContext):
#     answer = call.data
#     await state.update_data(city=answer)
#     question = questions["Q3"]
#     await call.message.answer(f'{question["question"]}',
#                               reply_markup=ReplyKeyboardRemove())
#     # await FSMTest.next()
#     await FSMTest.Q100.set()
