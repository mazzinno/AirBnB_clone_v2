#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''function that print text variable'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''display n if is anumber'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num2(n):
    '''display n if is anumber'''
    return render_template('5-number.html', test=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''displays “Number: n is even|odd'''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
