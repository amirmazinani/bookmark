import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from application import db


class Links(db.Model):
    __tablename__ = "links"

    # table columns
    link_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)

