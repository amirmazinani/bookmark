import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Link(db.Model):
    __tablename__ = "links"

    # table columns
    link_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    link = db.Column(db.Text, nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=0)
    visit_count = db.Column(db.Integer, default=0, nullable=False)
    # user_id is foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

