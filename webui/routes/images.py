""" General route """
from flask import render_template, Blueprint
from ..common import docker
import subprocess


view = Blueprint('images', __name__)


@view.route('/images', methods=['GET'])
def images():
    """ Index page """
    ps = subprocess.check_output('docker ps -a', shell=True).decode().split('\n')[1:]
    ps_obj = [docker.Container(raw) for raw in ps if raw]
    return render_template('images.html', ps=ps_obj)
