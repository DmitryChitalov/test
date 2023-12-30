from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_blog.config import Config
# from flask_bcrypt import Bcrypt
# from flask_mail import Mail
#
# db = SQLAlchemy()
# login_manager = LoginManager()
# bcrypt = Bcrypt()
# mail = Mail()
#app = Flask(__name__)
# app.config.from_object(Config)
#app.config.from_object(__name__)
#SECRET_KEY = b'\x143#\x1eV;\xc9\xa0\xecr\r\xd4/{b\n'
# config_class=Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    #app.config.from_object(__name__)
    #app.config.from_object(Config)
    #app.config.from_object(__name__)
    #db.init_app(app)
    #login_manager.init_app(app)
    #bcrypt.init_app(app)
    #mail.init_app(app)

    from flask_parser.flask_parser.flask_parser import parser_blueprint
    from flask_parser.authorization.auth import auth_blueprint

    #from flask_blog.main.routes import main
    #from flask_blog.users.routes import users
    #from flask_blog.posts.routes import posts
    #app.register_blueprint(main)
    #app.register_blueprint(users)
    #app.register_blueprint(posts)
    app.register_blueprint(parser_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
