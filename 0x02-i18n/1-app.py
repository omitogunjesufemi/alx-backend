#!/usr/bin/env python3
"""
Basic Flask App

Create a single / route and an index.html template that simply
outputs Welcome to Holberton as page title (<title>) and
Hello world as header (<h1>).
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())


@app.route('/', strict_slashes=False)
def index():
    """Welcome page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
