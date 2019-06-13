import jwt
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from app import db


class BaseModel(db.Model):
    """Base data model for all objects"""

    __abstract__ = True

    # define here __repr__ and json methods or any common method
    # that you need for all your models


class Users(BaseModel, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

# What is Encode? -> Creates our token for us

    def generate_token(self, user_id):
        try:
            # set up a payload with an expiration time
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            # create the byte string token using the payload and the SECRET key
            jwt_string = jwt.encode(
                payload,
                app.config.get('SECRET'),
                algorithm='HS256'
            )
            return jwt_string

        except Exception as e:
            # return an error in string format if an exception occurs
            return str(e)

    @staticmethod
    def decode_token(token):
        """Decodes the access token from the Authorization header."""
        try:
            # try to decode the token using our SECRET variable
            payload = jwt.decode(token, app.config.get('SECRET'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            # the token is expired, return an error string
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            # the token is invalid, return an error string
            return "Invalid token. Please register or login"

    def __repr__(self):
        return 'User: {}'.format(self.username)

class Bucketlist(BaseModel, db.Model):
    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.sessino.commit()
        

    def __repr__(self):
        return 'Bucketlist: {}'.format(self.title)

# DECODING IS LIKE MAKING SCENSE OUT OF THE ENCODED AREA
