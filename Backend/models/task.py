#!/usr/bin/python3
"""the Task class"""
from models import db
from models.BaseModel import BaseModel

class Task(db.Model, BaseModel):
    """Represents a task in the TaskVault"""
    __tablename__ = 'tasks'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.Datetime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
