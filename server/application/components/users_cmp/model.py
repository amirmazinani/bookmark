from sqlalchemy import Column, Integer, String

from application import db


class User(db.model):
    __tablename__ = "users"

    # table columns
