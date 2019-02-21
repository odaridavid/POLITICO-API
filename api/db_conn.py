import psycopg2
import os
from instance.config import application_config


# Get current environment
def db_uri():
    # Database URI as per environment
    if os.getenv("FLASK_ENV") is None:
        # return "dbname=politico_db_tests user=postgres password=politico host=localhost port=5432"
        return application_config['testing'].DATABASE_URI
    return application_config[os.getenv("FLASK_ENV")].DATABASE_URI


def connection():
    """Psycopg2 connection to db"""
    return psycopg2.connect(db_uri())


def db_connect():
    """Connection to database"""
    con = connection()
    return con


def create_tables():
    """Creates tables and commits to database"""
    con = psycopg2.connect(db_uri())
    cursor = con.cursor()
    # Execute queries
    for QUERY in schema():
        cursor.execute(QUERY)
    con.commit()


def drop_tables():
    """Drops tables when done"""
    con = psycopg2.connect(db_uri())
    cursor = con.cursor()
    cursor.execute("""DROP TABLE IF EXISTS users,offices,parties,candidates,votes CASCADE;""")
    con.commit()


def close_connection():
    """Closes connection when done"""
    con = psycopg2.connect(db_uri())
    con.close()


def schema():
    create_office = """CREATE TABLE IF NOT EXISTS offices( 
                    _id          SERIAL  PRIMARY KEY NOT NULL,
                    office_type   VARCHAR(100) NOT NULL,
                    office_name   VARCHAR(100) UNIQUE NOT NULL);"""
    create_users = "CREATE TABLE IF NOT EXISTS users(\
                       _id         SERIAL  PRIMARY KEY NOT NULL,\
                      firstname    VARCHAR(100) NOT NULL ,\
                      lastname     VARCHAR(100) NOT NULL,\
                      othername    VARCHAR(100) NOT NULL,\
                      email        VARCHAR  UNIQUE NOT NULL,\
                      phone_number VARCHAR(15) NOT NULL,\
                      passport_url VARCHAR NOT NULL,\
                      pass         VARCHAR NOT NULL, \
                      is_admin     BOOLEAN NOT NULL DEFAULT 'f');"
    create_parties = "CREATE TABLE IF NOT EXISTS parties(" \
                     "_id         SERIAL  PRIMARY KEY NOT NULL," \
                     "party_name  VARCHAR(50)   UNIQUE NOT NULL," \
                     "hq_address  VARCHAR(100)  NOT NULL," \
                     "logo_url    VARCHAR(200)  NOT NULL);"

    create_candidates = "CREATE TABLE IF NOT EXISTS candidates(" \
                        "_id       SERIAL NOT NULL UNIQUE ," \
                        "office    INTEGER NOT NULL DEFAULT 0," \
                        "party     INTEGER NOT NULL DEFAULT 0," \
                        "candidate INTEGER UNIQUE NOT NULL DEFAULT 0, " \
                        "CONSTRAINT office_fk FOREIGN KEY(office) REFERENCES offices(_id)," \
                        "CONSTRAINT party_fk FOREIGN KEY(party) REFERENCES parties(_id)," \
                        "CONSTRAINT candidate_fk FOREIGN KEY(candidate) REFERENCES users(_id)," \
                        "CONSTRAINT candidate_composite_key PRIMARY KEY(office,candidate));"

    create_votes = "CREATE TABLE IF NOT EXISTS votes(" \
                   "_id            SERIAL NOT NULL UNIQUE ," \
                   "created_on     DATE NOT NULL DEFAULT CURRENT_DATE," \
                   "created_by     INTEGER NOT NULL DEFAULT 0," \
                   "office         INTEGER NOT NULL DEFAULT 0, " \
                   "candidate      INTEGER NOT NULL DEFAULT 0, " \
                   "CONSTRAINT office_fk FOREIGN KEY(office) REFERENCES offices(_id)," \
                   "CONSTRAINT candidate_fk FOREIGN KEY(candidate) REFERENCES candidates(_id)," \
                   "CONSTRAINT voter_fk FOREIGN KEY(created_by) REFERENCES users(_id)," \
                   "CONSTRAINT vote_composite_key PRIMARY KEY(office,created_by));"
    return [create_users, create_office, create_parties, create_candidates, create_votes]
