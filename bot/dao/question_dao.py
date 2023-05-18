from bot.dao.models.question_model import Question



class QuestionDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Question).all()


