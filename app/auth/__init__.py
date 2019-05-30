from . import views
from flask import Blueprint

# This instant of a Blueprint thay represents the authentication
auth_blueprint = Blueprint('auth', __name__)
