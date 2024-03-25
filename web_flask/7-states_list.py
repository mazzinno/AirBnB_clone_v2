#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    '''
    Lists states from db
    '''
    state_dict = storage.all('State')
    state_list = []

    for state in state_dict.values():
        state_list.append(state)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
