from flask import Blueprint
from dashboard.models import User
from dashboard import db

api = Blueprint('api', __name__, url_prefix='/api')


# @api.route('auth')
# def auth():
