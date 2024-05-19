#!/usr/bin/python3
"""the Task class"""
import models
from models.BaseModel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class Task(BaseModel, Base):
    """Represents a task in the TaskVault"""
    __tablename__ = 'tasks'
    title = Column(String(80), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(String(128), ForeignKey('user.id'), nullable=False)
