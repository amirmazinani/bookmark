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
# from application.components.name import name
from application.components.users_cmp import users

# register blueprint
# app.register_blueprint(name)
app.register_blueprint(users)