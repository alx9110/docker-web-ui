from flask import request, render_template, Blueprint


view = Blueprint('dashboard', __name__)


@view.route('/', methods=['GET'])
def dashboard():
    return render_template('base.html')
