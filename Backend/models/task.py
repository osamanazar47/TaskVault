#!/usr/bin/python3
"""the Task class"""
from models import db


class Task(db.Model):
    """Represents a task in the TaskVault"""
    id = db.Column(db.String(128), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
