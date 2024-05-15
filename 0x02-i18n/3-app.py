#!/usr/bin/env python3
"""
Basic Flask App

Create a single / route and an index.html template that simply
outputs Welcome to Holberton as page title (<title>) and
Hello world as header (<h1>).
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config())


#@babel.localeselector
def get_locale() -> str:
    """Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)
@app.route('/', strict_slashes=False)
def index() -> None:
    """Welcome page"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
