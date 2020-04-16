from flask import Blueprint

lists = Blueprint('lists', __name__, url_prefix='/api/v1/user/<username>/list')

from . import view