from flask import render_template, redirect, request, url_for, g, flash
from flask_login import current_user, logout_user, login_required, login_user
from sqlalchemy.exc import DatabaseError
from werkzeug.security import generate_password_hash as hash_pswd

from book_review import app, lm, db
from book_review.forms import LoginForm, RegisterForm
from .models import Users


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Users.query.filter_by(nick=request.form['username']).first()
        if user is None or user.check_password(request.form['password']):
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(request.args.get('next') or url_for('search'))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        try:
            user = Users(request.form['username'], hash_pswd(request.form['password']), request.form['email'])
            db.session.add(user)
            db.session.commit()
        except DatabaseError:
            flash("Ups something bad happened :< Sorry")

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


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
