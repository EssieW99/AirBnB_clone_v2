#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello():
    """Prints out hello"""
    greeting = "Hello HBNB!"
    return greeting


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hello_2():
    """Prints out specified greeting"""
    output = "HBNB"
    return output


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def flask_var(text):
    """Ouputs predefined route text"""
    myvar = " ".join(text.split("_"))
    return (f"C {myvar}")


@app.route("/python", methods=['GET'], strict_slashes=False)
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def default_flask_var(text="is cool"):
    """Ouputs predefined route text"""
    myvar = " ".join(text.split("_"))
    return (f"Python {myvar}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
