#!/usr/bin/python3
'''Creates a /,  /hbnb, and /c/<text >routes'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''Sorts the / route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''Sorts the /hbnb route'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''Sorts the /c/<text> route'''
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(debug=True)
