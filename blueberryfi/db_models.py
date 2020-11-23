from datetime import datetime
from blueberryfi import db

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
        netname = db.Column(db.String(100))
        nettype = db.Column(db.String(100))
        netpass = db.Column(db.String(100))
        adblock = db.Column(db.String(100))
        adminname = db.Column(db.String(100))
        adminpass = db.Column(db.String(100))

        def __repr__(self):
            return '<User %r>' % self.adminname