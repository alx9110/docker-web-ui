""" General route """
from flask import render_template, Blueprint, session, redirect, flash
from webui.common.logger import logger
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
    client.containers.run(name.replace('sha256:', ''), detach=True, ports={'80/tcp': None})
    flash('Container is started', 'success')
    logger.info('{0} has been started'.format(name))
    return redirect('/images')


@view.route('/images/remove/<name>', methods=['GET'])
def remove_image(name):
    """ Remove some image """
    client = docker.client.from_env()
    try:
        client.images.remove(name.replace('sha256:', ''), force=True)
        flash('Image has been removed', 'success')
        logger.info('{0} has been deleted'.format(name))
        return redirect('/images')
    except docker.errors.APIError:
        flash(str(docker.errors.APIError.__doc__), 'danger')
        return redirect('/images')
