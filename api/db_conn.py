import psycopg2
import os
from instance.config import application_config
from .schema import CreateTables
from .schema import DropTables

# Get current environment
environment = os.getenv("FLASK_ENV")
# Database URI as per environment
db_uri = application_config[environment].DATABASE_URI


def db_connection():
    return psycopg2.connect(db_uri)


# Cursor to execute queries
def db_cursor():
    return db_connection().cursor()


def execute_creates_queries():
    # Loops through queries as it executes and finally commits
    for query in CreateTables.create_tables_queries():
        db_cursor().execute(query)
    db_connection().commit()


def execute_drop_queries():
    db_cursor().execute(DropTables.drop_tables())
    db_connection().commit()


def closing_connection(cursor):
    """Close connection in curson and db"""
    cursor.close()
    db_connection().close()
