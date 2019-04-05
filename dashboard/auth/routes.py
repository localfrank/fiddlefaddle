from dashboard.models import User
from flask import Blueprint, request, make_response, jsonify, current_app
from werkzeug.security import check_password_hash
import jwt
import datetime

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    """
    Register
    """
    pass


@auth.route('/login')
def login():
    """
    Login
    """
    credentials = request.authorization

    if not credentials or not credentials.username or not credentials.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!", charset="UTF-8"'})

    user = User.query.filter_by(username=credentials.username).first()

    if not user:
        return make_response('Username was not found!', 401, {'WWW-Authenticate': 'Basic realm="Username not found!", charset="UTF-8"'})

    if check_password_hash(user.password, credentials.password):
        token = jwt.encode({'public_id': user.public_id,
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Incorrect password!', 401, {'WWW-Authenticate': 'Basic realm="Password not correct!", charset="UTF-8"'})


@auth.route('/logout')
def logout():
    """
    Logout
    """
    pass
