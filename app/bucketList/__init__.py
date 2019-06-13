from flask import Blueprint

# This instance of a Blueprint that represents the authentication blueprint
bucketlist_blueprint = Blueprint('bucketlist', __name__)

from . import views
