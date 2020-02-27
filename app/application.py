from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")


@app.route("/<username>", methods=["POST"])
def user():
    return True


@app.route("/<username>/lists", methods=["POST"])
def lists():
    return True


@app.route("/<username>/posts", methods=["POST"])
def posts():
    return True


@app.route("/<username>/list/<int:list_id>", methods=["POST"])
def single_list():
    return True


@app.route("/<username>/post/<int:post_id>", methods=["POST"])
def single_post():
    return True


@app.route("/setting", methods=["POST"])
def setting():
    return True


@app.route("/login", methods=["POST"])
def login():
    return True


@app.route("/logout", methods=["POST"])
def logout():
    return True


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
