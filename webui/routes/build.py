""" General route """
from flask import render_template, Blueprint, request, flash, redirect
import subprocess


view = Blueprint('build', __name__)


@view.route('/build', methods=['POST'])
def build():
    """ Build page """
    repo = request.form['repo']
    repo_name = request.form['repo'].lstrip('https://github.com/').rstrip('.git')
    cmd = 'git clone {link} /tmp/{name}'.format(link=repo, name=repo_name)
    subprocess.call(cmd.split())
    # auto build
    cmd = 'docker build -t test-auto-build /tmp/{name}'.format(name=repo_name)
    subprocess.call(cmd.split())
    flash('Build success', 'success')
    return redirect('/')
