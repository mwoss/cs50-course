from psycopg2 import sql
import csv
from argparse import ArgumentParser


def is_file_valid(parser: ArgumentParser, file_path: str) -> str:
    if file_path.endswith('.csv'):
        return file_path
    parser.error("Invalid file extension. Script supports only CSV files")


def main():
    parser = ArgumentParser(description="Script for database population")
    parser.add_argument('connection-string', type=str,
                        help="Connection string in format: postgresql://HOST:PORT/DB_NAME")
    parser.add_argument('csv_file', type=lambda file: is_file_valid(parser, file), help="Path to CSV file")


if __name__ == '__main__':
    main()
