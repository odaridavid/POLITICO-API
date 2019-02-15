import psycopg2
import os
from instance.config import application_config
from .schema import CreateTables

# Get current environment
environment = os.getenv("FLASK_ENV")
# Database URI as per environment
db_uri = application_config[environment].DATABASE_URI


def db_connection():
    return psycopg2.connect(db_uri)


def db_cursor():
    return db_connection().cursor()


def execute_queries():
    db_cursor().execute(CreateTables.create_all_tables())
    db_connection().commit()
