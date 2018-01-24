""" General route """
import os
from flask import request, render_template, Blueprint, session
import docker
import time


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def dashboard():
    return 'ok'
