from argparse import ArgumentParser
from csv import DictReader

from psycopg2 import DatabaseError, DataError

from connection import PostgresConnection, INSERT_QUERIES


def is_file_valid(parser_obj: ArgumentParser, file_path: str) -> str:
    if file_path.endswith('.csv'):
        return file_path
    parser_obj.error("Invalid file extension. Script supports only CSV files")


def populate(table: str):
    with open(args.csv_file, 'rb') as csv_data:
        with PostgresConnection() as cursor:
            reader = DictReader(csv_data)
            for row in reader:
                cursor.execute(INSERT_QUERIES[table], row)


if __name__ == '__main__':
    parser = ArgumentParser(description="Script for database population")
    parser.add_argument('csv_file', type=lambda file: is_file_valid(parser, file), help="Path to CSV file")
    parser.add_argument('table_name', type=str, help="Name of table to populate")
    args = parser.parse_args()

    try:
        populate(args.table_name)
    except (DatabaseError, DataError) as err:
        print(err)
