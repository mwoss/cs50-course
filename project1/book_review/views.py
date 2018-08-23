from flask import render_template, redirect, request, url_for, g, flash
from flask_login import current_user, logout_user, login_required, login_user
from werkzeug.security import generate_password_hash as hash_pswd

from book_review import app, lm, db
from .models import Users


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    user = Users.query.filter_by(nick=request.form['username']).first()
    if user is None or user.check_password(request.form['password']):
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))

    login_user(user)
    return redirect(request.args.get('next') or url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    user = Users(request.form['username'], hash_pswd(request.form['password']), request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login'))


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


@lm.user_loader
def load_user(id: str):
    return Users.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
