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
    email = db.Column(db.String(512), unique=True)
    phone = db.Column(db.String(32), unique=True)
    bio = db.Column(db.Text, default="")
    password = db.Column(db.String(266), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    private = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    visit_count = db.Column(db.Integer, default=0)
    # foreign key references
    lists = db.relationship('List', backref='users', lazy='dynamic')
    posts = db.relationship('Post', backref='users', lazy='dynamic')
    links = db.relationship('Link', backref='users', lazy='dynamic')
