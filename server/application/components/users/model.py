import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class User(db.Model):
    __tablename__ = "users"

    # table columns
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(512), nullable=False, unique=True)
    first_name = db.Column(db.String(128), default="")
    last_name = db.Column(db.String(128), default="")
    gender = db.Column(db.Boolean)
    birthday = db.Column(db.DateTime)
    email = db.Column(db.String(512), nullable=False, unique=True)
    phone = db.Column(db.String(32), nullable=False, unique=True)
    bio = db.Column(db.Text)
    password = db.Column(db.String(512), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=0)
    visit_count = db.Column(db.Integer, default=0, nullable=False)
    # foreign key references
    lists = db.relationship('List', backref='users', lazy='dynamic')
    posts = db.relationship('Post', backref='users', lazy='dynamic')
    links = db.relationship('Link', backref='users', lazy='dynamic')
