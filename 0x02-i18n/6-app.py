#!/usr/bin/env python3
"""
Basic Flask App

Create a single / route and an index.html template that simply
outputs Welcome to Holberton as page title (<title>) and
Hello world as header (<h1>).
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Dict


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    user_locale = g.user.get("locale")
    if user_locale in app.config["LANGUAGES"]:
        return user_locale

    h_locale = request.headers.get("Accept-Language")
    if h_locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Dict:
    """
    Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """
    Use get_user to find a user if any, and set it as a global
    on flask.g.user
    """
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index() -> None:
    """Welcome page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
