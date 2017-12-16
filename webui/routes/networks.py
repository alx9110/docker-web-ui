""" General route """
from flask import render_template, Blueprint
import docker


view = Blueprint('networks', __name__)


@view.route('/networks', methods=['GET'])
def networks():
    """ Index page """
    client = docker.from_env()
    nets = client.networks.list()
    return render_template('networks.html', nets=nets)
