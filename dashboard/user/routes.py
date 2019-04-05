from flask import Blueprint, request, jsonify
from dashboard.models import User
from dashboard import db
from dashboard.auth.utils import token_required
import uuid
from werkzeug.security import generate_password_hash

user = Blueprint('user', __name__)


@user.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    """
    Get all users
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403

    users = User.query.all()
    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['admin'] = user.admin
        user_data['active'] = user.active
        user_data['api_user'] = user.api_user
        output.append(user_data)

    return jsonify({'users': output})


@user.route('/users/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    """
    Get one user against user id
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['admin'] = user.admin
    user_data['active'] = user.active
    user_data['api_user'] = user.api_user

    return jsonify({'user': user_data})


@user.route('/users', methods=['POST'])
@token_required
def create_user(current_user):
    """
    Create user
    """
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()),
                    username=data['username'], email=data['email'], password=hashed_password,
                    admin=False, active=True, api_user=data['api_user'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user ({}) created!'.format(data['username'])}), 200


@user.route('/users/<public_id>', methods=['PUT'])
@token_required
def update_user(current_user, public_id):
    """
    update user
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    data = request.get_json()
    user.admin = data['admin']
    user.active = data['active']
    user.api_user = data['api_user']
    db.session.commit()

    return jsonify({'message': 'The user ({}) has been updated!'.format(public_id)})


@user.route('/users/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    """
    Delete user
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403

    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found!'})
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user ({}) has been deleted!'.format(public_id)})
