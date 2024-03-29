#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", methods=["GET"], strict_slashes=False)
def list_states():
    """Returns a list of all states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", methods=["GET"], strict_slashes=False)
def list_states_with_id(id):
    """Returns a list of all states and their cities"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
