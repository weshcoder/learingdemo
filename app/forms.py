from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])