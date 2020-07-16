"""The web interface for ats_hacker."""

import os
from api.aggregator import aggregate
from flask import Flask, render_template, redirect, request, url_for
from web_server.forms.job_posting import JobListingForm


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/keywords', methods=['GET', 'POST'])
    def keywords():
        if request.method == 'POST':
            form = JobListingForm(request.form)
            keyword_counts = aggregate(form.posting.data)
            return render_template("keywords.html",
                                   keyword_counts=keyword_counts)
        else:
            return redirect(url_for('index'))

    return app
