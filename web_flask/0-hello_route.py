#!/usr/bin/python3
"""
0-hello_route.py
~~~~~~~~~~~~~~~~

This module implements a Flask web application with a single route that displays
"Hello HBNB!" when accessed.

Routes:
    /: Displays "Hello HBNB!"

Usage:
    - Run this module directly to start the Flask web application:
        ```
        python3 -m web_flask.0-hello_route
        ```
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.

    Returns:
        str: A greeting message.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
