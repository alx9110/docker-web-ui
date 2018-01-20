""" Config """
import os
from flask import current_app



_BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
        Default Config
    """
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    ROOT_LOGIN = ''
    ROOT_PASSWORD_HASH = ''


class Production(Config):
    """
        ProductionConfig
    """
    DEBUG = False


class Development(Config):
    """
        DevelopmentConfig
    """
    DEBUG = True
    ROOT_LOGIN = 'admin@docker.ui' # fake login
    ROOT_PASSWORD_HASH = 'b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342' # sha256 hash.hexdigest()


class Testing(Config):
    """
        TestingConfig
    """
    TESTING = True
    DEBUG = True


config = {
    'DEFAULT': Config,
    'PRODUCTION': Production,
    'DEVELOPMENT': Development,
    'TESTING': Testing
}


def get_config():
    """
        Return an application configuration
    """
    return current_app.config
