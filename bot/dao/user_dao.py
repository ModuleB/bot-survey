from bot.dao.models.user_model import User


class UserDAO():
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def save_user(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()