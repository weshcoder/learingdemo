from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegestrationForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired(), Length(min =2, max = 20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Login')   