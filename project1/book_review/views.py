from os import environ

from flask import render_template, redirect, request, url_for, g, flash, jsonify
from flask_login import current_user, logout_user, login_required, login_user
from requests import get as r_get
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.security import generate_password_hash as hash_pswd

from book_review import app, lm, db
from book_review.forms import LoginForm, RegisterForm, ReviewForm, SearchForm
from book_review.models import Reviews, Users, Books
from book_review.consts import GOODREAD_URL, BOOK_PER_SEARCH, GOODREAD_API


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Users.query.filter_by(nick=form.username.data).first()
        if user is None or user.check_password(form.password.data):
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(request.args.get('next') or url_for('home'))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        try:
            user = Users(nick=form.username.data, password=hash_pswd(form.password.data), email=form.email.data)
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


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for('search_result', query=form.search.data))

    return render_template('search.html', form=form)


@app.route('/search/<string:query>', methods=['GET'])
@login_required
def search_result(query: str):
    page = request.args.get('page', 1, type=int)
    search_res = Books.query \
        .filter((Books.title.ilike('%' + query + '%')) | (Books.isbn == query)) \
        .paginate(page, BOOK_PER_SEARCH, False)

    return render_template('search_result.html', query=query, books=search_res)


@app.route('/book/<string:isbn>', methods=['GET', 'POST'])
@login_required
def book_info(isbn: int):
    form = ReviewForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                review = Reviews(book_isbn=isbn, rating=form.rating.data, review=form.review.data,
                                 reviewer=current_user.nick)
                db.session.add(review)
                db.session.commit()
                return redirect(url_for('book_info', isbn=isbn))
            except IntegrityError:
                db.session.rollback()
                flash("Sorry, but you can write 1 comment per book")
            except ArithmeticError:
                flash("Ups our database have bad mood today :< Sorry")

    book = get_book_data(isbn)
    reviews = Reviews.query.filter_by(book_isbn=isbn).all()

    return render_template('book.html', book=book, reviews=reviews, form=form)


@app.route('/api/<string:isbn>', methods=['GET'])
def api_book_info(isbn: str):
    return jsonify(get_book_data(isbn))


@lm.user_loader
def load_user(id: str):
    return Users.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


def get_book_data(isbn):
    good_reads = r_get(GOODREAD_URL, params={'key': environ['GOODREAD_KEY'], 'isbns': isbn})

    if good_reads.status_code != 200:
        return {
            'error_message': "Internal error"
        }

    book = Books.get_as_dict(isbn=isbn)
    good_reads = good_reads.json()['books'][0]
    filtered_data = {key: good_reads[key] for key in GOODREAD_API}
    return {
        **book,
        **filtered_data
    }
