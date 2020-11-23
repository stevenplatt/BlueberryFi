from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    if request.form['password'] == 'blueberry' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
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
        return render_template('admin.html', creds=request.form['credential'])

    else:
        return render_template('admin.html')
