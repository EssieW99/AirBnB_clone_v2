#!/usr/bin/python3
""" starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template


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
    text_space = escape(text).replace('_', ' ')
    return f"C {text_space}"


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ displays 'Python' then value of the text"""
    text_space = escape(text).replace('_', ' ')
    return f"Python {text_space}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays 'n is a number if n is an int"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ displays "Number: n” inside the tag BODY"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """ displays "Number: n is odd or even” inside the tag BODY"""
    if n % 2 == 0:
        num = 'even'
    else:
        num = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
