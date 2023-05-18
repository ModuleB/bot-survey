from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

class ConfigClass:

    # ТОКЕН ТЕЛЕГРАМ БОТА
    BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str

    # НАСТРОЙКИ EMAIL УВЕДОМЛЕНИЯ
    EMAIL_NOTIFICATIONS_ENABLE = False
    # email получателя
    TO_EMAIL_ADDRESS = env.str("TO_EMAIL_ADDRESS")
    # email отправителя (логин)
    FROM_EMAIL_ADDRESS = env.str("FROM_EMAIL_ADDRESS")
    # Пароль от почтового ящика отправителя
    EMAIL_PASSWORD = env.str("EMAIL_PASSWORD")

    # НАСТРОЙКИ ТЕЛЕГРАМ УВЕДОМЛЕНИЯ
    TG_NOTIFICATIONS_ENABLE = True
    # ID админов в Телеграм для получения уведомлений
    ID_FOR_NOTIFICATIONS = env.str("ID_FOR_NOTIFICATIONS")

    # НАСТРОЙКИ БАЗЫ ДАННЫХ
    SAVE_TO_DB_ENABLE = True
    # Строка подключения к базе данных
    # DB_PATH = 'postgresql://postgres:postgres@localhost:5432/postgres'
    # DB_PATH = 'postgresql://aa:9541@localhost:5432/postgres'
    # DB_PATH = 'postgresql://bot:bot@172.19.0.2:5432/postgres'
    DB_PATH = 'postgresql://bot:bot@pg:5432/postgres'

    # Уровень логгера | по умолчанию включено INFO
    # LOG_LEVEL = "WARN"
    # LOG_LEVEL = "ERROR"
    # LOG_LEVEL = "CRITICAL"
    # LOG_LEVEL = "ERROR"

    # Проверка, проходил пользователь уже тест
    IS_ALREADY_PASSED_ENABLE = False

# Загрузка конфигурации
config = ConfigClass()






