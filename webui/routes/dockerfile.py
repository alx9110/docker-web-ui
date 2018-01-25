""" General route """
import os
from flask import request, render_template, Blueprint, session
import docker
import time
from webui.tasks import count_words_at_url
from rq import Queue
from redis import Redis


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def autobuild():
    """ Clone and build some git repo with Dockerfile """
    redis_conn = Redis()
    queue = Queue(connection=redis_conn)
    job = queue.enqueue(count_words_at_url, 'http://ya.ru')
    time.sleep(4)
    return job.status
