#!/usr/bin/python3
"""The configuration file for the Flask app"""

from os import getenv

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')
url = 'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER,
                                      HBNB_MYSQL_PWD,
                                      HBNB_MYSQL_HOST,
                                      HBNB_MYSQL_DB)


class Config:
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('SECRET_KEY') or 'you-will-never-guess'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
