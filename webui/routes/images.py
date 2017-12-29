""" General route """
from flask import render_template, Blueprint, session
import docker


view = Blueprint('images', __name__)


@view.route('/images', methods=['GET'])
def images():
    """ Index page """
    client = docker.client.from_env()
    images = client.images.list()
    user = session.get('login', None)
    return render_template('images.html', images=images, user=user)
