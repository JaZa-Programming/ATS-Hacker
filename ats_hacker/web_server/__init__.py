"""The web interface for ats_hacker."""

import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    @app.route('/')
    def index():
        return 'Welcome to ATS-Hacker!'

    return app
