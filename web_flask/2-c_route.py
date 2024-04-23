#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def texts(text):
    """ returns 'C' then value of the text"""
    text_space = {escape(text).replace('_', ' ')}
    return f"C {text_space}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
