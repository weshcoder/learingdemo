# /app/auth/views.py

from . import auth_blueprint

from flask.views import MethodView
from flask import make_response, request, jsonify, render_template, flash, redirect, url_for, session
from app.models import Users

from app.forms import RegistrationForm, LoginForm


class RegistrationView(MethodView):
    """This class registers a new user."""

    def get(self):
        """Handels Get requests for this view. Url ---> / auth/register"""
        form = RegistrationForm(request.form)
        return render_template("register.html", title='Register', form=form)

    def post(self):
        """Handle POST request for this view. Url ---> /auth/register"""

        # Query to see if the user already exists
        form = RegistrationForm(request.form)
        user = Users.query.filter_by(email=form.Email.data).first()

        if user == None:
            if form.validate():
                # There is no user so we'll try to register them
                try:
                    username = form.Username.data
                    email = form.Email.data
                    password = form.Password.data
                    user = Users(username=username, email=email, password=password)
                    user.save()

                    flash('Congratulations, you are now a registered user!')
                    return redirect(url_for('auth.login_view'))
                    # return a response notifying the user that they registered successfully

                except Exception as e:
                    # An error occured, therefore return a string message containing the error
                    flash("An error occured")

                    return render_template("register.html", title='Register', form=form)
        else:
            # There is an existing user. We don't want to register users twice
            # Return a message to the user telling them that they they already exist
            flash('A user with that email already exists')
            return render_template("register.html", title='Register', form=form)


class LoginView(MethodView):
    """This class-based view handles user login and access token generation."""
    def get(self):
        form = LoginForm(request.form)
        return render_template("login.html", title='Login', form=form)

    def post(self):
        """Handle POST request for this view. Url ---> /auth/login"""
        # Query to see if the user already exists
        form = LoginForm(request.form)
        user = Users.query.filter_by(email=form.Email.data).first()

        if user:
            if form.validate():
                try:
                    email = form.Email.data
                    password = form.Password.data
                    if user and user.password_is_valid(password):
                        # Generate the access token. This will be used as the authorization header
                        access_token = user.generate_token(user.id)
                        if access_token:
                            session['user_token'] = access_token
                            flash("Logged in!!")
                            return redirect(url_for("bucketlist.bucketlist_view"))

                    else: 
                        flash("Password or email is invalid")

                        return render_template("login.html", title='Login', form=form)        

                except Exception as e:
                    # An error occured , therefore return a string message containing the error
                    flash("An error occured")

                    return render_template("login.html", title='Login', form=form)
        else:
            # If the user does not excist We don't allow the login form
            flash("That user doesn't exist")
            return render_template("login.html", title='Login', form=form)

registration_view = RegistrationView.as_view('register_view')
login_view = LoginView.as_view('login_view')
# Define the rule for the registration url --->  /auth/register
# Then add the rule to the blueprint
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST', 'GET'])

# Define the rule for the registration url --->  /auth/register
# Then add the rule to the blueprint
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST', 'GET'])
