#!/usr/bin/python3
"""
initialize the models package
"""


from models.Engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
