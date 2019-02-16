class CreateTables:

    @staticmethod
    def create_tables_queries():
        # Serial will auto increment
        create_user = "CREATE TABLE users (" \
                      " _id         SERIAL  PRIMARY KEY NOT NULL," \
                      "firstname    VARCHAR(50) NOT NULL ," \
                      "lastname     VARCHAR(50) NOT NULL," \
                      "othername    VARCHAR(50) NOT NULL," \
                      "email        VARCHAR(50) UNIQUE NOT NULL," \
                      "phone_number INTEGER NOT NULL," \
                      "passport_url VARCHAR(50) NOT NULL," \
                      "is_admin     BOOLEAN NOT NULL DEFAULT 'f');"

        create_petition = "CREATE TABLE petitions(" \
                          "_id          SERIAL  PRIMARY KEY NOT NULL," \
                          "created_on   DATE NOT NULL DEFAULT CURRENT_DATE," \
                          "created_by   INTEGER NOT NULL REFERENCES users(_id)," \
                          "office       INTEGER NOT NULL REFERENCES offices(_id)," \
                          "body         VARCHAR(500) NOT NULL );"

        create_office = "CREATE TABLE office( " \
                        " _id          SERIAL  PRIMARY KEY NOT NULL," \
                        "office_type   VARCHAR(100) NOT NULL," \
                        "office_name   VARCHAR(100) UNIQUE NOT NULL);"

        create_parties = "CREATE TABLE parties(" \
                         "_id         SERIAL  PRIMARY KEY NOT NULL," \
                         "party_name  VARCHAR(50)   UNIQUE NOT NULL," \
                         "hq_address  VARCHAR(100)  NOT NULL," \
                         "logo_url    VARCHAR(200)  NOT NULL);"

        create_votes = "CREATE TABLE votes(" \
                       " _id          SERIAL  PRIMARY KEY NOT NULL," \
                       "created_on    DATE NOT NULL DEFAULT CURRENT_DATE," \
                       "created_by    INTEGER NOT NULL REFERENCES users(_id)  ," \
                       "office        INTEGER NOT NULL REFERENCES offices(_id), " \
                       "candidate     INTEGER NOT NULL REFERENCES  candidates(_id));"

        create_candidates = "CREATE TABLE candidates(" \
                            " _id          SERIAL  PRIMARY KEY NOT NULL," \
                            "office        INTEGER NOT NULL REFERENCES offices(_id) ," \
                            "party         INTEGER NOT NULL REFERENCES parties(_id)  ," \
                            "candidate     INTEGER NOT NULL REFERENCES  users(_id));"
        # Store queries in a list and loop over each
        query_list = [create_user, create_petition, create_office, create_candidates, create_votes, create_parties]
        return query_list


class DropTables:

    @staticmethod
    def drop_tables():
        drop_all = "DROP TABLE IF EXISTS users,petitions,offices,parties,votes,candidates CASCADE "
        return drop_all
