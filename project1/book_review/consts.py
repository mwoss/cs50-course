from os import environ

# goodread
GOODREAD_URL = "https://www.goodreads.com/book/review_counts.json"
GOODREAD_KEY = environ['GOODREAD_KEY']

# models
BOOK_PER_SEARCH = 10

GOODREAD_API = ('average_rating', 'reviews_count')
