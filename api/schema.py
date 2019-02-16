class CreateTables:

    @staticmethod
    def create_user_table():
        # Serial will auto increment
        create_table = "CREATE TABLE users (" \
                       " _id         SERIAL  PRIMARY KEY NOT NULL," \
                       "firstname    VARCHAR(50) NOT NULL ," \
                       "lastname     VARCHAR(50) NOT NULL," \
                       "othername    VARCHAR(50) NOT NULL," \
                       "email        VARCHAR(50) UNIQUE NOT NULL," \
                       "phone_number INTEGER NOT NULL," \
                       "passport_url VARCHAR(50) NOT NULL," \
                       "is_admin     BOOLEAN NOT NULL DEFAULT 'f');"
        return create_table

    @staticmethod
    def create_petition_table():
        create_petition = "CREATE TABLE petitions(" \
                          "_id          SERIAL  PRIMARY KEY NOT NULL," \
                          "created_on   DATE NOT NULL DEFAULT CURRENT_DATE," \
                          "created_by   INTEGER NOT NULL REFERENCES users(_id)," \
                          "office       INTEGER NOT NULL REFERENCES offices(_id)," \
                          "body         VARCHAR(500) NOT NULL );"
        return create_petition

    @staticmethod
    def create_office_table():
        create_office = "CREATE TABLE office( " \
                        " _id          SERIAL  PRIMARY KEY NOT NULL," \
                        "office_type   VARCHAR(100) NOT NULL," \
                        "office_name   VARCHAR(100) UNIQUE NOT NULL);"
        return create_office

    @staticmethod
    def create_parties_table():
        create_parties = "CREATE TABLE parties(" \
                         "_id         SERIAL  PRIMARY KEY NOT NULL," \
                         "party_name  VARCHAR(50)   UNIQUE NOT NULL," \
                         "hq_address  VARCHAR(100)  NOT NULL," \
                         "logo_url    VARCHAR(200)  NOT NULL);"
        return create_parties

    @staticmethod
    def create_votes_table():
        create_votes = "CREATE TABLE votes(" \
                       " _id          SERIAL  PRIMARY KEY NOT NULL," \
                       "created_on    DATE NOT NULL DEFAULT CURRENT_DATE," \
                       "created_by    INTEGER NOT NULL REFERENCES users(_id)  ," \
                       "office        INTEGER NOT NULL REFERENCES offices(_id), " \
                       "candidate     INTEGER NOT NULL REFERENCES  candidates(_id));"
        return create_votes

    @staticmethod
    def create_candidates_table():
        create_candidates = "CREATE TABLE candidates(" \
                            " _id          SERIAL  PRIMARY KEY NOT NULL," \
                            "office        INTEGER NOT NULL REFERENCES offices(_id) ," \
                            "party         INTEGER NOT NULL REFERENCES parties(_id)  ," \
                            "candidate     INTEGER NOT NULL REFERENCES  users(_id));"
        return create_candidates

    @classmethod
    def create_all_tables(cls):
        return cls.create_candidates_table().join(cls.create_office_table()).join(cls.create_parties_table()).join(
            cls.create_petition_table()).join(cls.create_votes_table()).join(cls.create_user_table())


class DropTables:

    @staticmethod
    def drop_user_table():
        drop_user = "DROP TABLE IF EXISTS users CASCADE "
        return drop_user

    @staticmethod
    def drop_petition_table():
        drop_petitions = "DROP TABLE IF EXISTS petitions  "
        return drop_petitions

    @staticmethod
    def drop_office_table():
        drop_offices = "DROP TABLE IF EXISTS offices CASCADE "
        return drop_offices

    @staticmethod
    def drop_parties_table():
        drop_parties = "DROP TABLE IF EXISTS parties CASCADE "
        return drop_parties

    @staticmethod
    def drop_votes_table():
        drop_votes = "DROP TABLE IF EXISTS votes "
        return drop_votes

    @staticmethod
    def drop_candidates_table():
        drop_candidates = "DROP TABLE IF EXISTS candidates CASCADE  "
        return drop_candidates

    @classmethod
    def drop_all_tables(cls):
        drop_all = "DROP TABLE IF EXISTS users,petitions,offices,parties,votes,candidates CASCADE "
        return drop_all
