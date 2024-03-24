#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.city import City


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


@app.route("/number_template/<n>", methods=['GET'], strict_slashes=False)
def temp_num(n):
    """Outputs predefined route number"""
    if n.isdigit():
        return render_template("5-number.html", n=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>", methods=['GET'], strict_slashes=False)
def temp_logic_num(n):
    """Outputs predefined route number"""
    if n.isdigit():
        return render_template("6-number_odd_or_even.html", n=n)
    else:
        abort(404)


@app.route("/cities_by_states", methods=["GET"], strict_slashes=False)
def list_states():
    """Returns a list of all states and their cities"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template(
        "8-cities_by_states.html", states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
