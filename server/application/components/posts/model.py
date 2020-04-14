import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Posts(db.Model):
    __tablename__ = "posts"

    # table columns
    post_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)

