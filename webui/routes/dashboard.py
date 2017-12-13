""" General route """
from flask import render_template, Blueprint
import docker


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    """ Index page """
    client = docker.from_env()
    containers = client.containers.list()
    return render_template('dashboard.html', containers=containers)
