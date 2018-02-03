""" General route """
from flask import render_template, Blueprint, session, redirect, flash, jsonify
from webui.common.logger import logger
import docker
import json


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    """ Index page """
    user = session.get('login', None)
    client = docker.from_env()
    containers = client.containers.list()
    status = {'count': len(containers),
             }
    detail = [json.loads(next(c.stats()), encoding='utf-8') for c in containers]
    # return jsonify(detail[0])
    logs = open('/var/log/dockerwebui.log', 'r').readlines()[::-1]
    return render_template('dashboard.html',
                           containers=containers,
                           user=user, status=status,
                           detail=detail,
                           logs=logs,
                          )


@view.route('/kill/<short_id>', methods=['GET'])
def kill(short_id):
    """ Kill container """
    client = docker.from_env()
    client.containers.get(short_id).kill()
    logger.info('{0} has been killed'.format(short_id))
    flash('Container has been killed', 'success')
    return redirect('/')
