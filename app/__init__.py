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

    # @app.route("/auth/login", methods=['GET', 'POST'])
    # def login():
    #     form = LoginForm(request.form)
    #
    #     if request.method == 'POST' and form.validate():
    #         email = form.Email.data
    #         password = form.Password.data
    #         user = Users.query.filter_by(email=email).first()
    #
    #         if user and user.password_is_valid(password):
    #             # Create a session for our user
    #             session["user"] = user
    #             flash(f'Congratulations, you logged in!')
    #             return redirect(url_for('yourbucketlist'))
    #
    #         flash(f'Email or password incorrect')
    #         return redirect(url_for('/auth/login'))
    #
    #     return render_template("login.html", title='Login', form=form)


    @app.route('/yourbucketlist')
    def yourbucketlist():
        user = session["user"]
        return render_template('bucketlist.html', user=user.username)

    @app.route('/auth/reset')
    def reset():
        return render_template('reset.html')

    # import authentication blurprint and register it on the app
    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
