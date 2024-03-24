#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", methods=["GET"], strict_slashes=False)
def list_states():
    """Returns a list of all states and their cities"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template(
        "8-cities_by_states.html", states=states, cities=cities)


@app.teardown_request
def teardown_db(exception):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
