import os
import json
from pathlib import Path

# with open('/etc/config.json') as config_file:
# config = json.load(config_file)


class Config:
    '''Default configuration'''
    # SECRET_KEY = config.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    # MONGO_URI = config.get('MONGO_URI')
    SECRET_KEY = "f9bf78b9a18ce6d46a0cd2b0b86df9da"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@mariadb/fiddlefaddle?charset=utf8"
    MONGO_URI = "mongodb://devone:devone@mongodb/fiddlefaddle"
