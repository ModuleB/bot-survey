from create.create_db import db_session
from bot.dao.user_dao import UserDAO
from bot.dao.question_dao import QuestionDAO
from bot.services.user_service import UserService
from bot.services.question_service import QuestionService


question_dao = QuestionDAO(db_session)
question_service = QuestionService(question_dao)

user_dao = UserDAO(db_session)
user_service = UserService(user_dao)

