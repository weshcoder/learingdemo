import os
from flask import Flask, render_template, flash, redirect, request, url_for, session
from flask_bcrypt import Bcrypt
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# intialialize sql-SQLAlchemy
db = SQLAlchemy()

from app.forms import RegistrationForm, LoginForm
from app.models import Users

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/about")
    def about():
        return render_template('about.html')

    # import authentication blurprint and register it on the app
    from .auth import auth_blueprint
    from .bucketList import bucketlist_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(bucketlist_blueprint)

    return app
