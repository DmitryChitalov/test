# from flask import Blueprint
# import sys
# import os
# import unittest
# import json
#
# sys.path.append(os.path.join(os.getcwd(), '..'))
# # print(os.path.join(os.getcwd(), '..'))
import multiprocessing as ml
#from flask_parser.parser_app import main as pr
# #from web_app import create_app
#
# from flask import Flask, render_template

from flask_parser import create_app


#SECRET_KEY = b'\x143#\x1eV;\xc9\xa0\xecr\r\xd4/{b\n'

#app = Flask(__name__)
#app.config.from_object(__name__)
#main = Blueprint('main', __name__)



# def create_app():
#     from .flask_parser.flask_parser import parser_blueprint
#     #from .authorization.auth import auth_blueprint
#     app.register_blueprint(parser_blueprint)
#     #app.register_blueprint(auth_blueprint)
#
#     return app

# @app.route("/")
# def root():
#     print("привет")
#     """
#        Функция обработки запроса к корневой странице
#     :return Страница Index
#     """
#     return render_template("index.html")
# @app.errorhandler(404)
# def not_found(e):
#     return render_template("404.html")

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.close()
#app = create_app()
if __name__ == "__main__":
    # Создать приложение Flask
    app = create_app()

    # Запустить парсер
    #par_service = ml.Process(name="HH Parser", target=pr.main)
    #par_service.start()


    # Запустить Flask приложение
    app.run()
