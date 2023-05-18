from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, DateTime, BIGINT, MetaData
from create.create_db import db, db_session, engine


class User(db):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    tg_id = Column(BIGINT)
    tg_username = Column(String)
    full_name = Column(String)
    age = Column(Integer)
    city = Column(String)
    email = Column(String)
    phone = Column(BIGINT)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.dt
    tg_id = fields.Int()
    tg_username = fields.Str()
    full_name = fields.Str()
    age = fields.Int()
    city = fields.Str()
    email = fields.Str()
    phone = fields.Int()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# db.metadata.create_all(engine)
# db_session.commit()