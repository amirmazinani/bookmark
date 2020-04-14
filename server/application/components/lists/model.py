import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Lists(db.Model):
    __tablename__ = "lists"

    # table columns
    list_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=0)
    visit_count = db.Column(db.Integer, default=0, nullable=False)
    posts_count = db.Column(db.Integer, default=0, nullable=False)
    share_count = db.Column(db.Integer, default=0, nullable=False)
    likes_count = db.Column(db.Integer, default=0, nullable=False)
    # user_id is foreign key


