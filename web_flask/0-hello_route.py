#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index(strict_slashes=False):
    """Web application must be listening on 0.0.0.0."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
