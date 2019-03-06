'''Models'''
from datetime import datetime
from chatterbox import db


class User(db.Model):
    '''User table'''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    bots = db.relationship('Bot', backref='account', lazy=True)

    def __repr__(self):
        return "User({}, {})".format(self.public_id, self.username)


class Bot(db.Model):
    '''Bot feature table'''
    __tablename__ = 'bot'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    date_registered = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'user.public_id'), nullable=False)

    def __repr__(self):
        return "Bot({}, {}, {})".format(self.name, self.description, self.active)
