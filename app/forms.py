from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(Form):
    Username = StringField('Username', render_kw={"class": "form-control", "placeholder":'Enter Username'}, validators=[DataRequired(), Length(min =2, max = 20)])
    Email = StringField('Email', render_kw={"class": "form-control", "placeholder":'Enter Email'}, validators=[DataRequired(), Email()])
    Password = PasswordField('Password', render_kw={"class": "form-control", "placeholder":'Enter Password'}, validators=[DataRequired()])
    Repeat_Password = PasswordField('Repeat_Password', render_kw={"class": "form-control", "placeholder":'Repeat Password'}, validators=[DataRequired(), EqualTo('Password')])
    Submit = SubmitField('Sign Up')

class LoginForm(Form):
    Email = StringField('Email', render_kw={"class": "form-control", "placeholder":'Enter Email'}, validators=[DataRequired(), Email()])
    Password = PasswordField('Password', render_kw={"class": "form-control", "placeholder":'Enter Password'}, validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Login')

class BucketListForm(Form):
    Title = StringField('Title', render_kw={"class": "form-control", "placeholder":'Enter Title' }, validators=[DataRequired(), Length(min=3, max=255)])
    Description = StringField('Description', render_kw={"class": "form-control", "placeholder":'Enter Description' })
