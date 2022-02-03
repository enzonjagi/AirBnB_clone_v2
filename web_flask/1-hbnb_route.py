#!/usr/bin/python3
'''Creates a / route'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''Sorts the / route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''Sorts the / route'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
