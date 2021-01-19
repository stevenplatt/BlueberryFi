import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blueberry.db'
db = SQLAlchemy(app)

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
        netname = db.Column(db.String(100))
        nettype = db.Column(db.String(100))
        netpass = db.Column(db.String(100))
        adblock = db.Column(db.String(100))
        adminuser = db.Column(db.String(100))
        adminpass = db.Column(db.String(100))

        def __repr__(self):
            return '<User %r>' % self.adminuser

import routes

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0')

# query format
# test = User.query.filter_by(adminuser='admin').first()