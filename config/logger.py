# pip install colorlog
from colorlog import ColoredFormatter
import logging

from config.config import ConfigClass


def logger_config(logger):

    try:
        if ConfigClass.LOG_LEVEL == "DEBUG":
            LOG_LEVEL = logging.DEBUG
        elif ConfigClass.LOG_LEVEL == "INFO":
            LOG_LEVEL = logging.INFO
        elif ConfigClass.LOG_LEVEL == "WARN":
            LOG_LEVEL = logging.WARN
        elif ConfigClass.LOG_LEVEL == "CRITICAL":
            LOG_LEVEL = logging.CRITICAL
        elif ConfigClass.LOG_LEVEL == "ERROR":
            LOG_LEVEL = logging.ERROR

    except:
        LOG_LEVEL = logging.INFO


    LOGFORMAT = " %(log_color)s[%(levelname)s] %(asctime)s - %(name)s - %(message)s (%(filename)s:%(lineno)d)%(reset)s"

    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(LOGFORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(stream)