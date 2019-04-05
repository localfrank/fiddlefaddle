from functools import wraps
from flask import request, jsonify, current_app
from dashboard.models import User
import jwt


def token_required(f):
    """
    Decorator
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            token_data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_user = User.query.filter_by(
                public_id=token_data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
