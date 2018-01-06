""" General route """
import os
import hashlib
import sqlite3
from flask import Blueprint, session, jsonify


view = Blueprint('user', __name__)


@view.route('/token', methods=['GET'])
def get_token():
    """ Token """
    user = session.get('login', None)
    if user:
        credentials = {'Token': hashlib.sha256(os.urandom(8)).hexdigest()}
        return jsonify(credentials)
    else:
        error = {'Error': 'Who are you?'}
        return jsonify(error)
