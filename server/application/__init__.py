from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Development

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt_manager = JWTManager(app)

@app.route('/')
def home():
    return 'app is running\n'

# import blueprint
from application.components.users import users
from application.components.links import links
from application.components.lists import lists
from application.components.posts import posts

# register blueprint
app.register_blueprint(users)
app.register_blueprint(links)
app.register_blueprint(lists)
app.register_blueprint(posts)