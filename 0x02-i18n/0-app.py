#!/usr/bin/env python3
"""Basic Flask setup."""
from flask import Flask, render_template

# Initiarize a flask app.
app = Flask(__name__)


@app.route('/')
def index():
    """Home page of our flask application."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
