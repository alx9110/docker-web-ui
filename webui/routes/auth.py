""" Auth components """
import os
import hashlib
from flask import request, render_template, Blueprint, session, redirect, flash


view = Blueprint('auth', __name__)


@view.route('/auth', methods=['GET'])
def auth():
    """ Auth page """
    return render_template('signin.html')


@view.route('/acl', methods=['GET'])
def check_acl():
    """ Check login/password """
    login = request.args.get('login')
    raw_password = request.args.get('password')
    pass_hash = 'b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7f159c67b90fb4b7342'
    if hashlib.sha256(bytearray(raw_password, encoding='utf-8')).hexdigest() == pass_hash:
        session['login'] = login
        flash('Hello {login}'.format(login=login), 'success')
        return redirect('/')
    flash('Invalid credentials', 'danger')
    return redirect('/auth')


@view.route('/signout', methods=['GET'])
def sign_out():
    """ Sign out """
    session.pop('login', None)
    return redirect('/')
