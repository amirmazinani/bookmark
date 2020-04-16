from flask import Blueprint

links = Blueprint('links', __name__, url_prefix='/api/v1/user/<username>/link')

from . import view