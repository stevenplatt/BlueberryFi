from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/admin')
def admin(): # was previously named "profile()"
    return render_template('admin.html', name=current_user.name)