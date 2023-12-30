import configparser as cfg

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = cfg.ConfigParser()
config.read("./flask_parser/hh_config.ini")

engine = create_engine(config["SQLite"]["path"])
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine)


#
#
# @app.teardown_appcontext
# #def shutdown_session(exception=None):
#     #db_session.close()
#
#
# def create_db():
#     Base.metadata.drop_all(engine)
#     # Создание новых таблиц
#     Base.metadata.create_all(engine)
#     db_session.close()
