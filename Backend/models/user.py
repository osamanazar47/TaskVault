#!/usr/bin/python3
"""the User class"""
from werkzeug.security import generate_password_hash, check_password_hash
from Backend.models import db

class User(db.Model):
    """class represents a user in TaskVault"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
