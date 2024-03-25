#!/usr/bin/python3
"""the flask model"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """refrech data"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """it returns all states in the database"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
