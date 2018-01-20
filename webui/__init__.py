""" Init """
from flask import Flask
from .routes import dashboard, networks, images, dockerfile, auth, user, build
from .config import config


__version__ = '0.0.1'


def create_app(environment):
    """ Create app """
    app = Flask(__name__)
    app.config.from_object(config[environment])

    # Blueprints register
    app.register_blueprint(auth.view)
    app.register_blueprint(dashboard.view)
    app.register_blueprint(networks.view)
    app.register_blueprint(images.view)
    app.register_blueprint(dockerfile.view)
    app.register_blueprint(build.view)
    # User profile include
    app.register_blueprint(user.view)

    return app
