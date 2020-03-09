from flask import Flask

app = Flask(__name__)


@app.route("/api/v1/", methods=["GET"])
def home():
    """ home page """
    return True


@app.route("/api/v1/<username>", methods=["GET", "PUT"])
def user():
    """ get user data and update user data """
    return True


@app.route("/api/v1/<username>/lists", methods=["GET", "POST"])
def lists():
    """ get all lists of user and create a list for user """
    return True


@app.route("/api/v1/<username>/posts", methods=["GET", "POST"])
def posts():
    """ get all posts of user and create a post for user """
    return True


@app.route("/api/v1/<username>/lists/<int:list_id>", methods=["GET", "PUT"])
def single_list():
    """ get all posts of a user's list or edit user's list data """
    return True


@app.route("/api/v1/<username>/posts/<int:post_id>", methods=["GET", "PUT"])
def single_post():
    """ get post data of user or edit this """
    return True


@app.route("/api/v1/login", methods=["POST"])
def login():
    """ login func """
    return True


@app.route("/api/v1/logout", methods=["POST"])
def logout():
    """ logout func """
    return True


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
