from flask import Blueprint

lists = Blueprint('lists', __name__, url_prefix='/')

from . import view