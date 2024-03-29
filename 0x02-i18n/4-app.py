#!/usr/bin/env python3
"""Basic Flask setup."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


# Initiarize a flask app.
app = Flask(__name__)


class Config(object):
    """Configure Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine best language match based on supported languages
    """
    # Check if the 'locale' parameter is present in the request URL
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        # If the requested locale is supported, return it
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    # If the 'locale' parameter is not present or not supported,
    # resort to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Home page of our flask application."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
