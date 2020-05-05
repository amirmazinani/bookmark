from flask import Blueprint

posts = Blueprint('posts', __name__, url_prefix='/api/v0/user/<username>/list/<list_id>/post')

from . import view