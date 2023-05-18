from bot.dao.models.question_model import Question
from create.create_db import db_session, db, engine

# Создаем таблицы
db.metadata.create_all(engine)
db_session.commit()


def create_data():
    question1 = Question(state="Q1", question="Напишите ваше ФИО")
    question2 = Question(state="Q2", question="Сколько вам лет? (только число)")
    question3 = Question(state="Q3", question="В каком городе вы живете?")
    question4 = Question(state="Q4", question="Напишите ваш email")
    question5 = Question(state="Q5", question="Напишите ваш номер телефона (начните с 7)")

    db_session.add_all([question1, question2, question3, question4, question5])
    db_session.commit()