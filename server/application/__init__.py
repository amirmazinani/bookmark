from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from application.config import Development

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt_manager = JWTManager(app)

@app.route('/')
def home():
    return {'message': 'Hello World'}

# import blueprint
# from application.components.name import name

# register blueprint
# app.register_blueprint(name)