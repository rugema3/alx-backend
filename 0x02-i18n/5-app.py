#!/usr/bin/env python3
"""Basic Flask setup."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


# Initiarize a flask app.
app = Flask(__name__)

# Mock user database table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Configure Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


def get_user():
    """
    Returns user information based on the 'login_as'
    parameter in the request URL.

    Returns:
        dict or None: A dictionary containing user information if
        'login_as' parameter is present
        and valid, otherwise returns None.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Execute before all other functions."""
    current_user = get_user()
    g.current_user = current_user


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
    return render_template('5-index.html', )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
