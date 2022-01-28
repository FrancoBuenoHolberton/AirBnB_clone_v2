#!/usr/bin/python3
"""
0.Hello Flask!
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Hellobnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hellobnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cprint(text):
    """Cprintisfun"""
    txt = text.replace("_", " ")
    return 'C ' + txt


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Python is cool"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Verify if is a number"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000')
