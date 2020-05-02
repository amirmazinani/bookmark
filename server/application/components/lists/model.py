import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class List(db.Model):
    __tablename__ = "lists"

    # table columns
    list_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(512), nullable=False)
    description = db.Column(db.Text, default="")
    deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)
    posts_count = db.Column(db.Integer, default=0)
    share_count = db.Column(db.Integer, default=0)
    likes_count = db.Column(db.Integer, default=0)
    # foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    # foreign key references
    posts = db.relationship('Post', backref='lists', lazy='dynamic')


