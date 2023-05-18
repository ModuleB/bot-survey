import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from bot.handlers import test, admin, common
from config.config import config
from config.logger import logger_config

# Настройка логирования в stdout
logger = logging.getLogger(__name__)
logger_config(logger)


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_commands(bot: Bot):
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Вывести справку"),
        BotCommand("test", "Пройти опрос"),
        BotCommand("about", "Информация о боте"),
    ]
    await bot.set_my_commands(commands)


async def main():

    logger.info("Starting bot")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Регистрация хэндлеров
    common.register_handlers_common(dp)
    admin.register_handlers_admin(dp)
    test.register_handlers_admin(dp)


    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    try:
        await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
        await dp.start_polling(bot)

    finally:
        s = await bot.get_session()
        await s.close()


if __name__ == '__main__':
    asyncio.run(main())
