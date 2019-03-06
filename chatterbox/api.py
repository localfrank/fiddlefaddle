# from flask import current_app, Blueprint, g, jsonify, request, make_response
# from flaskr.db import get_mongo, get_alchemy
# from flaskr.auth import login_required
# from bson.json_util import dumps
# import uuid
# from werkzeug.security import generate_password_hash, check_password_hash
# from flaskr.models import Account, Bot
# import jwt
# import datetime
# from functools import wraps

# bp = Blueprint('api', __name__, url_prefix='/api')
# db = get_alchemy()


# @bp.route('/bots', methods=['GET'])
# @login_required
# def get_bots():
#     mongo = get_mongo()
#     bots = mongo.db.bot.find()
#     return dumps(bots)


# @bp.route('/account/<public_id>', methods=['GET'])
# @token_required
# def account(current_account, public_id):
#     '''Get account against public id'''
#     account = Account.query.filter_by(public_id=public_id, active=True).first()
#     if not account:
#         return jsonify({'message': 'Not found. No account associate with {} as public ID'.format(public_id)})

#     account_data = {}
#     account_data['public_id'] = account.public_id
#     account_data['name'] = account.name
#     account_data['email'] = account.email
#     account_data['password'] = account.password  # Hashed password
#     account_data['active'] = account.active
#     return jsonify({'account': account_data})


# @bp.route('/account', methods=['GET'])
# @token_required
# def get_all_accounts(current_account):
#     '''Get all accounts via root user'''
#     if not current_account.root:
#         return jsonify({'message': 'Only root account can perform this function!'})

#     accounts = Account.query.all()
#     output = []
#     for account in accounts:
#         account_data = {}
#         account_data['public_id'] = account.public_id
#         account_data['name'] = account.name
#         account_data['email'] = account.email
#         account_data['password'] = account.password  # Hashed password
#         account_data['active'] = account.active

#         output.append(account_data)
#     return jsonify({'accounts': output})


# @bp.route('/account', methods=['POST'])
# @token_required
# def create_account(current_account):
#     '''create account'''
#     data = request.get_json()
#     hashed_password = generate_password_hash(data['password'], method='sha256')
#     new_account = Account(public_id=str(uuid.uuid4(
#     )), name=data['name'], email=data['email'], password=hashed_password, active=True)
#     db.session.add(new_account)
#     db.session.commit()
#     return jsonify({'message': 'New account created!'})


# @bp.route('/account/<name>', methods=['PUT'])
# @token_required
# def activate_account(current_account, name):
#     '''Activate account against account name'''
#     account = Account.query.filter_by(name=name, active=False).first()
#     if not account:
#         return jsonify({'message': 'Not found. No account associate with {} as account name'.format(name)})

#     account.activate = True
#     db.session.commit()
#     return jsonify({'message': 'Account {} has been activated!'.format(name)})


# @bp.route('/account<name>', methods=['DELETE'])
# @token_required
# def inactivate_account(current_account, name):
#     '''Set account inactive instead of deleting it for future'''
#     account = Account.query.filter_by(name=name, active=True).first()
#     if not account:
#         return jsonify({'message': 'Not found. No account associate with {} as account name'.format(name)})

#     account.activate = False
#     db.session.commit()
#     return jsonify({'message': 'Account {} has been inactivated!'.format(name)})


# @bp.route('/login')
# def login():
#     '''
#     API login
#     return 401 (Unauthorized) when failure
#     '''
#     auth = request.authorization
#     if not auth or not auth.username or not auth.password:
#         return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

#     account = Account.query.filter_by(name=auth.username, active=True).first()
#     if not account:
#         # return jsonify({'message': 'No active account found!'})
#         return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

#     if check_password_hash(account.password, auth.password):
#         token = jwt.encode({'public_id': account.public_id, 'exp': datetime.datetime.utcnow(
#         ) + datetime.timedelta(minutes=15)}, current_app.config['SECRET_KEY'])
#         return jsonify({'token': token.decode('UTF-8')})

#     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None

#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']

#         if not token:
#             return jsonify({'message': 'Token is missing.'}), 401

#         try:
#             data = jwt.decode(token, current_app.config['SECRET_KEY'])
#             current_account = Account.query.filter_by(
#                 public_id=data['public_id']).first()
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 401

#         return f(current_account, *args, **kwargs)

#     return decorated
