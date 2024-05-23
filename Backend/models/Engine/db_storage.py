#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models import db


class DBStorage:
    """The database class"""
    def __init__(self):
        self.__engine = db.engine
        self.__session = db.session

    def add(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def delete(self, obj):
        self.__session.delete(obj)
        self.__session.commit()

    def all(self, cls=None):
        if cls:
            return self.__session.query(cls).all()
        return self.__session.query().all()

    def get(self, cls, id):
        return self.__session.query(cls).get(id)