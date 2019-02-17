import psycopg2
import os
from instance.config import application_config


# Get current environment
def db_uri():
    # Database URI as per environment
    if os.getenv("FLASK_ENV") is None:
        # return "dbname=politico_db_tests user=postgres password=politico host=localhost port=5432"
        return "postgresql://postgres:politico@localhost:5432/politico_db_tests"
    return "postgresql://postgres:politico@localhost:5432/politico_db_tests"


def connection():
    try:
        return psycopg2.connect(db_uri())
    except psycopg2.OperationalError:
        return 'Connection Error'


def db_connect():
    """Connection to database"""
    con = connection()
    return con


def create_tables():
    """Creates tables and commits to database"""
    con = psycopg2.connect(db_uri())
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                       _id         SERIAL  PRIMARY KEY NOT NULL,\
                      firstname    VARCHAR(100) NOT NULL ,\
                      lastname     VARCHAR(100) NOT NULL,\
                      othername    VARCHAR(100) NOT NULL,\
                      email        VARCHAR  UNIQUE NOT NULL,\
                      phone_number VARCHAR(15) NOT NULL,\
                      passport_url VARCHAR NOT NULL,\
                      pass         VARCHAR NOT NULL, \
                      is_admin     BOOLEAN NOT NULL DEFAULT 'f');")
    con.commit()


def drop_tables():
    """Drops tables when done"""
    con = psycopg2.connect(db_uri())
    cursor = con.cursor()
    cursor.execute("""DROP TABLE IF EXISTS users;""")
    con.commit()


def close_connection():
    """Closes connection when done"""
    con = psycopg2.connect(db_uri())
    con.close()
