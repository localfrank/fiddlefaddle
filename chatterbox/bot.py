from flask import Blueprint
from chatterbox.models import Bot
from chatterbox import db


bp = Blueprint('bot', __name__, url_prefix='/bot')
