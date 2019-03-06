from flask import Blueprint
from chatterbox.models import User
from chatterbox import db

users = Blueprint('user', __name__, url_prefix='/user')


@users.route('add')
def add_user():
    user = User(public_id='123123', username='test user',
                email='test@gmail.com', password='123123', active=True)
    db.session.add(user)
    db.session.commit()
    return 'hello'
