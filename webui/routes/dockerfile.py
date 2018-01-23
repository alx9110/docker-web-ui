""" General route """
import os
from flask import request, render_template, Blueprint, session
import docker
import time
from rq import Queue
from redis import Redis
from tasks import count_words_at_url


redis_conn = Redis()
queue = Queue(connection=redis_conn)


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def dashboard():
    """ Index page """
    client = docker.from_env()
    plh = \
    """
    FROM ubuntu:14.04
    MAINTAINER Alexander Telkov <alx9110@yandex.ru>
    RUN apt-get update
    RUN apt-get install -y nginx
    RUN echo 'Hi, I am in your container'
            >/usr/share/nginx/html/index.html
    EXPOSE 80
    """
    job = queue.enqueue(count_words_at_url, 'http://ya.ru')
    user = session.get('login', None)
    return str(job.id)


@view.route('/status/<id>')
def upload_file(id):
    """ Dockerfile upload """
    job = queue.fetch_job(id)
    return str(job.result)
