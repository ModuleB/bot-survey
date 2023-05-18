from bot.dao.models.question_model import questions_schema
from run import logger


class QuestionService:
    def __init__(self, dao):
        self.dao = dao

    def get_questions(self):
        try:
            data = questions_schema.dump(self.dao.get_all())
            questions = {}
            for item in data:
                questions[item["state"]] = item["question"]
            return questions
        except Exception as e:
            logger.error(f'Database error\n{e}')






