#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Strict_slashes=False in your route definition."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Must be listening on 0.0.0.0, port 5000."""
    return "HBNB"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
