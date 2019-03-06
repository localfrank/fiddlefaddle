import os


class Config:
    '''Default configuration'''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MONGO_URI = os.environ.get('MONGO_URI')
