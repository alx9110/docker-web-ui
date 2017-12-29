""" General route """
from flask import render_template, Blueprint, session, redirect, flash
import docker


view = Blueprint('images', __name__)


@view.route('/images', methods=['GET'])
def images():
    """ Index page """
    client = docker.client.from_env()
    images = client.images.list()
    user = session.get('login', None)
    return render_template('images.html', images=images, user=user)


@view.route('/images/run/<name>', methods=['GET'])
def run_image(name):
    """ Run container from image """
    client = docker.client.from_env()
    client.containers.run(name, detach=True, ports={'80/tcp': None})
    flash('Container is started', 'success')
    return redirect('/images')
