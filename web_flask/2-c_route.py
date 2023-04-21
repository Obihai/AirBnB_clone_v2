#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
   """Return a given string"""
   return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
   """Returns a given string"""
   return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =5000, debug=None)
