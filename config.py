# -*- coding: utf-8 -*-

# Python
from os import getenv
from datetime import timedelta


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    APP_PORT = getenv('APP_PORT')
    DEBUG = getenv('DEBUG')
    MONGODB_HOST = getenv('MONGODB_URI') or 'mongodb://localhost:27017/database'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=int(getenv('JWT_ACCESS_TOKEN_EXPIRES', 20))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(getenv('JWT_REFRESH_TOKEN_EXPIRES', 30))
    )


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
