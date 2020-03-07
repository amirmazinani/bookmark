from flask import Flask, render_template

app = Flask(__name__)


@app.route("/api/v1/", methods=["GET"])
def home():
    return True


@app.route("/api/v1/<username>", methods=["GET", "PUT"])
def user():
    return True


@app.route("/api/v1/<username>/lists", methods=["GET"])
def lists():
    return True


@app.route("/api/v1/<username>/posts", methods=["GET"])
def posts():
    return True


@app.route("/api/v1/<username>/lists/<int:list_id>", methods=["GET", "PUT", "POST"])
def single_list():
    return True


@app.route("/api/v1/<username>/posts/<int:post_id>", methods=["GET", "PUT", "POST"])
def single_post():
    return True


@app.route("/api/v1/login", methods=["POST"])
def login():
    return True


@app.route("/api/v1/logout", methods=["POST"])
def logout():
    return True


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
