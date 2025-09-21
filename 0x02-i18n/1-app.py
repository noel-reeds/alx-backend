#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from werkzeug.utils import import_string


app = Flask(__name__)
cfg = import_string('config.Config')()
app.config.from_object(cfg)
babel = Babel(app)


@app.route('/')
def index():
    """renders index files"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
