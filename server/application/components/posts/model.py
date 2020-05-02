import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Post(db.Model):
    __tablename__ = "posts"

    # table columns
    post_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(512), nullable=False)
    link = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, default="")
    deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)
    share_count = db.Column(db.Integer, default=0)
    likes_count = db.Column(db.Integer, default=0)
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.list_id'), nullable=False)

