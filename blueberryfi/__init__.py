import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(12)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db = SQLAlchemy(app)

    db.init_app(app)

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
        netname = db.Column(db.String(100))
        nettype = db.Column(db.String(100))
        netpass = db.Column(db.String(100))
        adblock = db.Column(db.String(100))
        adminname = db.Column(db.String(100))
        adminpass = db.Column(db.String(100))

        def __repr__(self):
            return '<User %r>' % self.adminname

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app