from flask import Blueprint

users = Blueprint('users', __name__, url_prefix='/api/v0/user')

from . import view