#!/usr/bin/python3
"""The configuration file for the Flask app"""

from os import getenv

TV_MYSQL_USER = getenv('TV_MYSQL_USER')
TV_MYSQL_PWD = getenv('TV_MYSQL_PWD')
TV_MYSQL_HOST = getenv('TV_MYSQL_HOST')
TV_MYSQL_DB = getenv('TV_MYSQL_DB')
url = 'mysql+mysqldb://{}:{}@{}/{}'.format(TV_MYSQL_USER,
                                      TV_MYSQL_PWD,
                                      TV_MYSQL_HOST,
                                      TV_MYSQL_DB)


class Config:
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('SECRET_KEY') or 'you-will-never-guess'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
