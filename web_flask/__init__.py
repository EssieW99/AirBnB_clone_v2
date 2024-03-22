#!/usr/bin/python3
"""Creates necessary configs for flask app"""
from flask import Flask


def create_app():
    """Creates a flask app instance"""
    app = Flask(__name__)
    return app
