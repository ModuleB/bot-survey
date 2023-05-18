from run import logger
from config.config import config
from utils.send_email import send_email


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        try:
            return self.dao.get_all()
        except Exception as e:
            logger.error(f'Database error\n{e}')

    def save_data(self, data):
        if config.SAVE_TO_DB_ENABLE:
            try:
                self.dao.save_user(data)
                logger.info(f"Id {data['tg_id']} saved to database")
            except Exception as e:
                logger.error(f'Database error\n{e}')





    def send_email(self, message, subject):
        if config.EMAIL_NOTIFICATIONS_ENABLE:
            if send_email(subject, message):
                print("\033[32m{}\033[0m".format(f"{subject} email sent"))

    def is_already_passed(self, id):
        if config.IS_ALREADY_PASSED_ENABLE:
            data = self.get_data()
            for i in data:
                if int(i) == id:
                    return False
                else:
                    return True
        else:
            return True


