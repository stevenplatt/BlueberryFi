from flask import render_template, url_for, flash, redirect, request, session, abort 
from blueberryfi import app, db
from blueberryfi.db_models import User
import socket

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
        return render_template('admin.html')
