#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from werkzeug.utils import import_string


cfg = import_string('1-app.Config')()
app = Flask(__name__)
babel = Babel(app)
app.config.from_object(cfg)


@app.route('/')
def index():
    """renders index files"""
    return render_template("0-index.html")
