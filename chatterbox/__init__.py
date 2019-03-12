import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from chatterbox.config import Config

db = SQLAlchemy()
mongo = PyMongo()


def create_app(test_config=None):
    '''Application factory'''
    app = Flask(__name__, instance_relative_config=True)
    # Loading default config
    app.config.from_object(Config)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    mongo.init_app(app)

    from chatterbox.user import users
    app.register_blueprint(users)

    with app.app_context():
        db.create_all()

    return app
