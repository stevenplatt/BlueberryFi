from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return render_template('index.html', creds=request.form['credential'])
    else:
        return redirect(url_for('login'))
