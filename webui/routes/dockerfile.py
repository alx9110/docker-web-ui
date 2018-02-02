""" General route """
from flask import request, render_template, Blueprint, session, flash
from webui.tasks import build_from_git
from rq import Queue
from redis import Redis


view = Blueprint('dockerfile', __name__)


@view.route('/dockerfile', methods=['GET'])
def home():
    """ Clone and build some git repo with Dockerfile """
    return render_template('dockerfile.html')

@view.route('/dockerfile', methods=['POST'])
def autobuild():
    """ Clone and build some git repo with Dockerfile """
    url = request.form.get('url').strip()
    try:
        redis_conn = Redis()
        queue = Queue(connection=redis_conn)
        job = queue.enqueue(build_from_git, url)
        flash('Auto build running | {0}'.format(job.status), 'info')
    except:
        flash('Auto build tools is not installed or not running', 'danger')
    return render_template('dockerfile.html')
