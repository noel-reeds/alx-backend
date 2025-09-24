#!/usr/bin/env python3
"""Get locale from request"""
from typing import Optional, Dict
from flask import _, g, request, Flask, render_template
from flask_babel import Babel
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


@app.before_request
def get_user() -> Optional[Dict]:
    """Mock logging in"""
    try:
        user_id = int(request.args.get("login_as"))
        if user_id in users.keys():
            g.user = users.get(user_id)
            return g.user
        return None
    except Exception as error:
        print(_("Not a valid number!"))
        return None


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
    (name := g.user.get('name') if hasattr(g, "user") else None)
    return render_template("4-index.html", user_name=name)


if __name__ == "__main__":
    app.run(debug=True)
