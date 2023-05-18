from sqlalchemy import text

from create.create_db import db_session
from utils.print_color import print_red, print_green

def check_db():

    try:
        db_session.execute(text('SELECT 1'))
        print_green("Соединение с базой данных установлено")

    except Exception as e:
        print_red("База данных недоступна")
        print_red(e)