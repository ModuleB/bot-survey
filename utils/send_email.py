# https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python

import smtplib
from email.message import EmailMessage
from config.config import config

def send_email(subject, message):
    try:

        if config.FROM_EMAIL_ADDRESS is None or config.EMAIL_PASSWORD is None:
            # no email address or password
            # something is not configured properly
            print("\033[31m{}\033[0m".format("Did you set email address and password correctly?"))
            return False

        # create email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = config.FROM_EMAIL_ADDRESS
        msg['To'] = config.TO_EMAIL_ADDRESS
        msg.set_content(message)

        # export email
        with smtplib.SMTP_SSL('smtp.yandex.ru', 465) as smtp:
            smtp.login(config.FROM_EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            smtp.send_message(msg)
        return True

    except Exception as e:
        print("\033[31m{}\033[0m".format("Problem during export email"))
        print("\033[31m{}\033[0m".format(f"{str(e)}"))
    return False


# # Адрес получателя
# to = 't3841@yandex.ru'
#
# # Тема письма
# subject = "subject"
#
# # Текст письма
# message = "HELLO FROM PYTHON"
#
# if send_email(to, subject, message):
#     print("Message sent")
