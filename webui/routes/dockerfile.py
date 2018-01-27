""" General route """
import os
from flask import request, render_template, Blueprint, session
import docker
import time
from webui.tasks import build_from_git
from rq import Queue
from redis import Redis


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def autobuild():
    """ Clone and build some git repo with Dockerfile """
    redis_conn = Redis()
    queue = Queue(connection=redis_conn)
    job = queue.enqueue(build_from_git, 'https://github.com/alx9110/docker-auto-build.git')
    time.sleep(4)
    return job.status
