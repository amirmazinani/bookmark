from flask import Blueprint

lists = Blueprint('lists', __name__, url_prefix='/api/v0/user/<username>/list')

from . import view