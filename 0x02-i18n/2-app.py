#!/usr/bin/env python3
"""Get locale from request"""
from flask import request, Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retrieves lang-setting"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Renders a page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
