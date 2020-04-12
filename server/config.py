import json

with open("./config.json") as cg:
    config = json.load(cg)


class Base():
    SQLALCHEMY_DATABASE_URI = config["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    SECRET_KEY = config["SECRET_KEY"]


class Development(Base):
    ENV = "development"


class Production(Base):
    ENV = "production"
