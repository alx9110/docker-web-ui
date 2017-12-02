""" General route """
from flask import render_template, Blueprint
from ..common import docker


view = Blueprint('images', __name__)


@view.route('/images', methods=['GET'])
def images():
    """ Index page """
    return render_template('images.html')