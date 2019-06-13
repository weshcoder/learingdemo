from . import bucketlist_blueprint

from flask.views import MethodView
from flask import make_response, request, jsonify, render_template, flash, redirect, url_for
from app.models import Bucketlist

from app.forms import BucketListForm


class BucketlistView(MethodView):
    def get(self):
        form = BucketListForm(request.form)
        return render_template("bucketlist", title="Bucketlist", form=form)

bucketlist_view = BucketlistView.as_view('bucketlist_view')

bucketlist_blueprint.add_url_rule(
    '/bucketlist',
    view_func=bucketlist_view,
    methods=['POST', 'GET'])
