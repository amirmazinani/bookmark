from . import users

from .model import User


@users.route('/<username>/', methods=['GET'])
def get_user_lists(username):
    return f"{username}\n"
