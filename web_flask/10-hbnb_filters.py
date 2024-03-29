#!/usr/bin/python3
"""Creates a basic python route"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", methods=["GET"], strict_slashes=False)
def list_filters():
    """Returns a list of all filters on the page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Performs cleanup tasks by closing the db connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
