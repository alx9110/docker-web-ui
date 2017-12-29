""" General route """
from flask import render_template, Blueprint, session
import docker


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    """ Index page """
    user = session.get('login', None)
    client = docker.from_env()
    containers = client.containers.list()
    return render_template('dashboard.html', containers=containers, user=user)
