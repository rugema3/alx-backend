<h1>0x02. i18n</h1>
<img src='img/babel.jpeg'>

<h1>Resources</h1>

<li><a href="https://intranet.alxswe.com/rltoken/fBpGjDt2BFuBFiz-jwublQ">Flask-Babel</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/9ocHNLN1lSTW3ioCNGCzbA">pytz</a></li>
<h1>Tasks</h1>
<h3>0. Basic Flask app</h3>

<p>First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title <pre>(<title>) </pre>and “Hello world” as header <pre>(<h1>)</pre>.
</p>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x02-i18n</li>
<li>File: 0-app.py, templates/0-index.html</li>
 
<h3>1. Basic Babel setup</h3>
<p>
Install the Babel Flask extension:</p>
<pre>
$ pip3 install flask_babel==2.0.0

</pre>
<p>
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.
</p>
<p>
In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
</p>
<p>
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
</p>
<p>
Use that class as config for your Flask app.
</p>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x02-i18n</li>
<li>File: 1-app.py, templates/1-index.html</li>
  
<h3>2. Get locale from request</h3>
<p>
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
</p>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x02-i18n</li>
<li>File: 2-app.py, templates/2-index.html</li>
 
<h3>3. Parametrize templates</h3>
<p>
Use the </b>_ </b>or <b>gettext</b> function to parametrize your templates. Use the message IDs home_title and home_header.
</p>
<p>
Create a babel.cfg file containing
</p>
<pre>
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
</pre>
<p>
Then initialize your translations with
</p>
<pre>
$ pybabel extract -F babel.cfg -o messages.pot .

</pre>
<p>
and your two dictionaries with
</p>
<pre>
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr

</pre>
<p>
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:
</p>
<table border="i">
<tr>
    <th>msgid</th>
    <th>English</th>
    <th>French</th>
</tr>
<tr>
    <td style="color: red;">home_title</td>
    <td style="color: red;">"Welcome to Holberton"</td>
    <td style="color: red;">"Bienvenue chez Holberton"</td>
 <tr>
    <td style="color: red;">home_header</td>
    <td style="color: red;">"Hello world!"</td>
    <td style="color: red;">"Bonjour monde!"</td>
</tr>

</table>
<p>
Then compile your dictionaries with
</p>
<pre>
$ pybabel compile -d translations

</pre>
<p>
Reload the home page of your app and make sure that the correct messages show up.
</p>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x02-i18n</li>
<li>File: 3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo</li>
  
4. Force locale with URL parameter
mandatory
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].

Visiting http://127.0.0.1:5000/?locale=fr should display this level 1 heading: 

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 4-app.py, templates/4-index.html
 
5. Mock logging in
mandatory
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid	English	French
logged_in_as	"You are logged in as %(username)s."	"Vous êtes connecté en tant que %(username)s."
not_logged_in	"You are not logged in."	"Vous n'êtes pas connecté."
Visiting http://127.0.0.1:5000/ in your browser should display this:



Visiting http://127.0.0.1:5000/?login_as=2 in your browser should display this: 

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 5-app.py, templates/5-index.html
 
6. Use user locale
mandatory
Change your get_locale function to use a user’s preferred local if it is supported.

The order of priority should be

Locale from URL parameters
Locale from user settings
Locale from request header
Default locale
Test by logging in as different users



Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 6-app.py, templates/6-index.html
 
7. Infer appropriate time zone
mandatory
Define a get_timezone function and use the babel.timezoneselector decorator.

The logic should be the same as get_locale:

Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 7-app.py, templates/7-index.html
 
8. Display the current time
#advanced
Based on the inferred time zone, display the current time on the home page in the default format. For example:

Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28

Use the following translations

msgid	English	French
current_time_is	"The current time is %(current_time)s."	"Nous sommes le %(current_time)s."
Displaying the time in French looks like this:



Displaying the time in English looks like this:



Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: app.py, templates/index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po