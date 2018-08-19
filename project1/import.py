import logging
from argparse import ArgumentParser
from csv import DictReader, Error
from psycopg2 import DatabaseError, DataError
from psycopg2.extras import execute_values
from book_review.utils.connection import PostgresConnection, INSERT_QUERIES

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def is_file_valid(parser_obj: ArgumentParser, file_path: str) -> str:
    if file_path.endswith('.csv'):
        return file_path
    parser_obj.error("Invalid file extension. Script supports only CSV files")


def populate(table: str):
    with open(args.csv_file, 'r') as csv_data:
        with PostgresConnection() as cursor:
            logging.info("Inserting data. That can take some time")
            headers = next(csv_data).strip().split(',')
            cursor.copy_from(file=csv_data, table=table, sep=',', columns=headers)


if __name__ == '__main__':
    parser = ArgumentParser(description="Script for database population")
    parser.add_argument('csv_file', type=lambda file: is_file_valid(parser, file), help="path to CSV file")
    parser.add_argument('table_name', type=str, help="name of table to populate")
    args = parser.parse_args()

    try:
        logging.info(f"Start populating table {args.table_name} with data")
        populate(args.table_name)
        logging.info("Data inserted to table")
    except (DatabaseError, DataError, Error) as exc:
        logging.error(exc)
    except KeyError:
        logging.error(f"Insert query for table: {args.table_name} doesnt exist")
