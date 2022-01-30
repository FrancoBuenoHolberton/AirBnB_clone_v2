#!/usr/bin/python3
""" Flask """

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/state_list', strict_slashes=False)
def print_states():
    """Hellobnb"""
    states_save = storage.all('State')
    return render_template('7-states_list.py', states_save=states)

