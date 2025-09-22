#!/usr/bin/env python3
"""Basic Babel setup"""
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configurations"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')


@app.route("/")
def index():
    """Renders index page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
