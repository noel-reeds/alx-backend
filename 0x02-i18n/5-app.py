#!/usr/bin/env python3
"""Get locale from request"""
from typing import Optional, Dict
from flask import g, request, Flask, render_template
from flask_babel import _, Babel
conf = __import__('1-app').Config


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(conf)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """Mock logging in"""
    try:
        user_id = int(request.args.get("login_as"))
        if user_id in users.keys():
            return users.get(user_id)
        return None
    except Exception as error:
        print(_("Not a valid number!"))
        return None


@app.before_request
def before_request():
    """Executed before all other functions."""
    user = get_user()
    if user:
        g.__setattr__("user", user)


@babel.localeselector
def get_locale() -> Optional[str]:
    """Retrieves lang-setting"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """Renders a page"""
    if hasattr(g, "user"):
        name = g.user.get('name')
    else:
        name = None
    return render_template("5-index.html", username=name)


if __name__ == "__main__":
    app.run(debug=True)
