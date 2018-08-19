import logging
from os.path import abspath

from psycopg2 import connect
from psycopg2.sql import SQL
from psycopg2.extras import DictCursor
from yaml import load, YAMLError

INSERT_QUERIES = {
    'books': SQL("INSERT INTO books (isbn, author, title, publication_year) "
                 "VALUES (%(isbn)s, %(author)s, %(title)s, %(year)s) ")
}


class PostgresConnection:
    def __init__(self):
        self._connection = connect(dsn=self._get_connection_string())

    def __enter__(self) -> DictCursor:
        return self._connection.cursor(cursor_factory=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.commit()
        self._connection.close()

    @staticmethod
    def _get_connection_string():
        creds = None
        with open(abspath("config.yml")) as yml_file:
            try:
                creds = load(yml_file)['postgresql']
            except YAMLError as exc:
                logging.error(exc)

        return f"postgres://{creds['user']}:{creds['password']}@{creds['host']}{creds['port']}/{creds['database']}"
