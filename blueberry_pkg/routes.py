from flask import render_template, url_for, flash, redirect, request, session, abort 
from blueberry_pkg import app, db, User
import socket

@app.route("/login", methods=['POST'])
def login():
    account = User.query.filter_by(adminuser='admin').first()
    if request.form['adminpass'] == account.adminpass:
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

    else:
        config = User.query.filter_by(adminuser='admin').first()
        return render_template('admin.html', netname=config.netname, nettype=config.nettype, netpass=config.netpass, adblock=config.adblock, adminuser=config, adminpass=config.adminpass)

@app.route('/update', methods=["POST"])
def update(): 
        netname = request.form.get("netname")
        nettype = request.form.get("nettype")
        netpass = request.form.get("netpass")
        adblock = request.form.get("adblock")
        adminpass = request.form.get("adminpass")

        update = User.query.filter_by(adminuser='admin').first()
        update.netname = netname
        update.nettype = nettype
        update.netpass = netpass
        update.adblock = adblock
        update.adminpass = adminpass

        db.session.commit()

        return redirect("/")
