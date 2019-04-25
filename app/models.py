from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

class BaseModel(db.Model):   
    """Base data model for all objects"""

    __abstract__ = True

    # define here __repr__ and json methods or any common method
    # that you need for all your models

class YourModel(BaseModel, db.Model):
    """ model for one of your table """  

    __tablename__ = 'firstable'
    
    id = db.Column(db.Integer, primary_key = True)
#     #define your model



class Users(BaseModel, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    def __init__(self, username, email, password):
        self.username = username  
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)   

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return 'User: {}'.format(self.username)
          
