from . import bucketlist_blueprint

from flask.views import MethodView
from flask import make_response, request, jsonify, render_template, flash, redirect, url_for
from app.models import Bucketlist

from app.forms import BucketListForm


class BucketlistView(MethodView):
    def get(self):
        return render_template("bucketlist.html ")

bucketlist_view = BucketlistView.as_view('bucketlist_view')

bucketlist_blueprint.add_url_rule(
    '/bucketlist',
    view_func=bucketlist_view,
    methods=['POST', 'GET'])
