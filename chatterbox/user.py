from flask import Blueprint
from chatterbox.models import User
from chatterbox import db

users = Blueprint('user', __name__, url_prefix='/user')


@users.route('add')
def add_user():
    user = User(public_id='123125', username='test user 2',
                email='test2@gmail.com', password='123123', active=True)
    db.session.add(user)
    db.session.commit()
    return 'hello'
