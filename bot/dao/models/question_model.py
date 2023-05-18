from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, MetaData
from create.create_db import db, engine, db_session


class Question(db):
    __tablename__= "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String, nullable=False)
    question = Column(String, nullable=False)


class QuestionSchema(Schema):
    id = fields.Int(dump_only=True)
    state = fields.Str()
    question = fields.Str()


question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)

# Создаем таблицы
metadata = MetaData()
# db.metadata.create_all(engine)
# db_session.commit()


