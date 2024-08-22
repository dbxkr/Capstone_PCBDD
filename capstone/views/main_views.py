from flask import Blueprint, url_for, session, render_template, current_app
from werkzeug.utils import redirect

from capstone import db
from capstone.models import User

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/select', methods=('GET', 'POST'))
def select():
    return render_template('main.html')

@bp.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('auth.login'))
    elif user_id == 1:
        return redirect(url_for('process.report'))
    else:
        return redirect(url_for('main.select'))