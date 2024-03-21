#!/usr/bin/python3
"""Creates a basic python route"""
from __init__ import create_app


app = create_app()


@app.route("/", methods=['GET'], strict_slashes=False)
def hello():
    """Prints out hello"""
    greeting = "Hello HBNB!"
    return greeting


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)