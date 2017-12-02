""" Init """
from flask import Flask
from .routes import dashboard
from .config import config


__version__ = '0.0.1'


def create_app(environment):
    """ Create app """
    app = Flask(__name__)
    app.config.from_object(config[environment])

    # Blueprints register
    app.register_blueprint(dashboard.view)

    return app
