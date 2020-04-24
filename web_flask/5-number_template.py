#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """Strict_slashes=False in your route definition."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Must be listening on 0.0.0.0, port 5000."""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text, strict_slashes=False):
    """Replace underscore _ symbols with a space."""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """Replace underscore _ symbols with a space."""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """Display “n is a number” only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Display a HTML page only if n is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
