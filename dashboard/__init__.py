import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from dashboard.config import Config

db = SQLAlchemy()
mongo = PyMongo()


def create_app(config_class=Config):
    '''Application factory'''
    app = Flask(__name__)
    # Loading default config
    app.config.from_object(Config)

    db.init_app(app)
    mongo.init_app(app)

    from dashboard.auth.routes import auth
    app.register_blueprint(auth)
    from dashboard.user.routes import user
    app.register_blueprint(user)
    from dashboard.project.routes import project
    app.register_blueprint(project)

    # from dashboard.api.routes import api
    # app.register_blueprint(api)

    with app.app_context():
        db.create_all()
        db.session.commit()

    @app.route("/")
    def hello_world():
        return "Hello World!"

    return app
