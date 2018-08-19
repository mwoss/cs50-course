from flask import render_template, redirect, url_for, g
from flask_login import current_user, logout_user, login_required

from book_review import app, lm


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    pass


@app.route('/register')
def register():
    pass


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/search')
@login_required
def search():
    pass


@app.route('/book/<string:isbn>', methods=['GET', 'POST'])
@login_required
def book_info(isbn: int):
    pass


@app.before_request
def before_request():
    g.user = current_user
