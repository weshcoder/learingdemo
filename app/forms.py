from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    Username = StringField('Username', render_kw={"class": "form-control", "placeholder":'Enter Username'}, validators=[DataRequired(), Length(min =2, max = 20)])
    Email = StringField('Email', render_kw={"class": "form-control", "placeholder":'Enter Email'}, validators=[DataRequired(), Email()])
    Password = PasswordField('Password',render_kw={"class": "form-control", "placeholder":'Enter Password'},validators=[DataRequired()])
    Repeat_Password = PasswordField('Repeat_Password',render_kw={"class": "form-control", "placeholder":'Repeat Password'}, validators=[DataRequired(), EqualTo('Password')])
    Submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Login')   

