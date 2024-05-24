#!/usr/bin/python3
"""the Task class"""
from . import db
from .BaseModel import BaseModel

class Task(BaseModel):
    """Represents a task in the TaskVault"""
    __tablename__ = 'tasks'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
