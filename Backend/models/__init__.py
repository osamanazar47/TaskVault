#!/usr/bin/python3
"""
initialize the models package
"""


from models.Engine import DBStorage
storage = DBStorage()
storage.reload()