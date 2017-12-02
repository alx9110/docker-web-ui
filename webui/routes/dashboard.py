""" General route """
from flask import render_template, Blueprint
from ..common import docker
import subprocess


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    """ Index page """
    ps = subprocess.check_output('docker ps', shell=True).decode().split('\n')[1:]
    ps_obj = [docker.Container(raw) for raw in ps if raw]
    return render_template('dashboard.html', ps=ps_obj)
