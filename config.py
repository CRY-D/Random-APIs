
from os import path
basedir = path.abspath(path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'db.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        path.join(path.abspath(path.dirname(__file__)), 'db.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True


class ProductionConfig(BaseConfig):
    # Production specific config
    DEBUG = False
