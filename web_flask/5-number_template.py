#!/usr/bin/python3
'''Creates a /,  /hbnb, /c/<text> ,and /python/<text> routes'''

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
def python_alone():
    '''Sorts the /python/<text> route'''
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    '''Sorts the /python/<text> route'''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''Sorts the /number/<n> route'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    '''Sorts the /number_template/<n> route'''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
