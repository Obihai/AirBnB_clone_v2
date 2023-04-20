#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask

app = Flask('__name__')

@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Return a string"""
    return 'Hello HBNB'

if __name__ == '__main__':
    """listening on 0.0.0.0, port 5000"""
    app.run(host='0.0.0.0', port=5000)
