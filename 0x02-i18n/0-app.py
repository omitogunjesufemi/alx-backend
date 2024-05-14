#!/usr/bin/env python3
"""
Basic Flask App

Create a single / route and an index.html template that simply
outputs Welcome to Holberton as page title (<title>) and
Hello world as header (<h1>).
"""
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """Welcome page"""
    title = "Welcome to Holberton"
    header = "Hello world"
    return render_template("index.html", title=title,
                           header=header)


if __name__ == "__main__":
    app.run()
