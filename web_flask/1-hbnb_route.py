#!/usr/bin/python3
"""
0.Hello Flask!
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Hi """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hiholbie"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000')
