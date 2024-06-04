#!/usr/bin/python3
"""the Task class"""
from . import db
from .BaseModel import BaseModel

class Task(BaseModel):
    """Represents a task in the TaskVault"""
    __tablename__ = 'tasks'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        task_dict = super().to_dict()

        # Adding Task-specific fields
        task_dict.update({
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'user_id': self.user_id,
            'completed': self.completed
        })
        return task_dict
