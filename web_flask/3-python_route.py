#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnbtext(text):
    """returns HBNB!"""
    processed_text = text.replace('_', ' ')
    return f'C {processed_text}'


@app.route('/python/<text>', strict_slashes=False)
def pythontext(text):
    """returns HBNB!"""
    processed_text = text.replace('_', ' ')
    return f'Python {processed_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
