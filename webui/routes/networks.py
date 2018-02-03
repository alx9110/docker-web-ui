""" General route """
from flask import render_template,\
                  Blueprint,\
                  flash,\
                  request,\
                  redirect,\
                  jsonify,\
                  session,\
                  current_app
import docker
from webui.common.logger import logger


view = Blueprint('networks', __name__)


@view.route('/networks', methods=['GET'])
def networks():
    """ Network list """
    client = docker.from_env()
    nets = client.networks.list()
    return render_template('networks.html', nets=nets)


@view.route('/networks/create', methods=['GET'])
def network_create():
    """ Network create """
    client = docker.from_env()
    name = request.args.get('net_name')
    client.networks.create(name)
    flash('Network <strong>{name}</strong> has been created'.format(name=name), 'success')
    return redirect('/networks')


@view.route('/networks/delete/<name>', methods=['GET'])
def network_remove(name=None):
    """ Remove network """
    client = docker.from_env()
    client.networks.get(name).remove()
    flash('network <{name}> has been remove'.format(name=name), 'success')
    return redirect('/networks')


@view.route('/networks/inspect/<name>', methods=['GET'])
def network_inspect(name=None):
    """ Network inspect """
    client = docker.from_env()
    inspect = client.networks.get(name).attrs
    return jsonify(inspect)
