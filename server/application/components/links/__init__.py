from flask import Blueprint

links = Blueprint('links', __name__, url_prefix='/')

from . import view