from flask import render_template, url_for, flash, redirect, request, session, abort 
from blueberryfi import app, db
from blueberryfi.db_models import User
import socket

def get_host_ip():
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name) 
    return host_ip

@app.route("/login", methods=['POST'])
def login():
    if request.form['adminpass'] == 'blueberry':
        session['logged_in'] = True
    else:
        flash('Invalid Password')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/', methods=['GET','POST'])
def home():
    if not session.get('logged_in'):
        return render_template('login.html')

    elif request.method == 'POST':
        return render_template('admin.html', adminuser='admin')

    else:
        my_ip = get_host_ip()
        return render_template('admin.html', ip=my_ip)
