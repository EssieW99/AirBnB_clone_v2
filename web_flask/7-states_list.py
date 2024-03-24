#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


@app.route("/states_list", methods=["GET"], strict_slashes=False)
def list_states():
    """Returns a list of all states"""
    state_info = []
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


teardown_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
