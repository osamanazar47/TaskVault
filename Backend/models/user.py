#!/usr/bin/python3
"""the User class"""
import models
from models.BaseModel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, Base):
    """Represents a user in the TaskVault"""
    __tablename__ = 'users'
    name = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=True)
    tasks = relationship('Task', backref='user', cascade='all, delete, delete-orphan', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
