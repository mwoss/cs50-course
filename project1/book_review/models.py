from werkzeug.security import check_password_hash

from book_review import db


class Users(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    nick = db.Column('nick', db.String(30), unique=True, index=True, nullable=False)
    email = db.Column('email', db.String(50), unique=True, index=True, nullable=False)
    password = db.Column('password', db.String(64), nullable=False)

    def __init__(self, nick, password, email):
        self.nick = nick
        self.password = password
        self.email = email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Reviews(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    book_isbn = db.Column('book_isbn', db.String(13), unique=True, index=True, nullable=False)
    rating = db.Column('rating', db.Integer, nullable=False)
    review = db.Column('review', db.String(2000), nullable=False)
    reviewer = db.Column('reviewer', db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __init__(self, book_isbn, rating, review, reviewer):
        self.book_isbn = book_isbn
        self.rating = rating
        self.review = review
        self.reviewer = reviewer

    def __repr__(self):
        return f'<Review for book: {self.book_isbn}\n{self.username}>'


class Books(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    isbn = db.Column('isbn', db.String(13), unique=True, index=True, nullable=False)
    author = db.Column('author', db.String(200))
    title = db.Column('title', db.String(200), nullable=False)
    publication_year = db.Column('publication_year', db.Integer)

    def __init__(self, isbn, author, title, publication_year):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publication_year = publication_year

    def __repr__(self):
        return f'<Book: {self.title}, isbn:{self.isbn}>'
