import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Lists(db.Model):
    __tablename__ = "lists"

    # table columns
    list_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)

