#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, abort


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
    """Outputs predefined route text"""
    myvar = " ".join(text.split("_"))
    return (f"C {myvar}")


@app.route("/python", methods=['GET'], strict_slashes=False)
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def default_flask_var(text="is cool"):
    """Outputs predefined route text"""
    myvar = " ".join(text.split("_"))
    return (f"Python {myvar}")


@app.route("/number/<n>", methods=['GET'], strict_slashes=False)
def is_var_num(n):
    """Outputs predefined route number"""
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
