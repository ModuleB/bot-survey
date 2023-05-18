from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config.config import config


db = declarative_base()
engine = create_engine(config.DB_PATH, pool_pre_ping=True)
SwssionClass = sessionmaker(bind=engine)
db_session = SwssionClass()


