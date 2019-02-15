class CreateTables:

    @staticmethod
    def create_user_table():
        # Serial will auto increment
        create_table = "CREATE TABLE users {" \
                       " _id          SERIAL  PRIMARY KEY NOT NULL," \
                       "firstname    VARCHAR(50) NOT NULL ," \
                       "lastname     VARCHAR(50) NOT NULL," \
                       "othername    VARCHAR(50) NOT NULL," \
                       "email        VARCHAR(50) NOT NULL," \
                       "phone_number INTEGER(15) NOT NULL," \
                       "passport_url VARCHAR(50) NOT NULL," \
                       "is_admin     BOOLEAN NOT NULL};"
        return create_table

    @staticmethod
    def create_petition_table():
        create_petition = "CREATE TABLE petitions{" \
                          "_id          SERIAL  PRIMARY KEY NOT NULL," \
                          "created_on   DATE NOT NULL DEFAULT CURRENT_DATE," \
                          "created_by   INTEGER NOT NULL REFERENCES users(_id)," \
                          "office       INTEGER NOT NULL REFERENCES offices(_id)" \
                          "body         VARCHAR(500) NOT NULL };"
        return create_petition

    @staticmethod
    def create_office_table():
        create_office = "CREATE TABLE office{ " \
                        " _id          SERIAL  PRIMARY KEY NOT NULL," \
                        "office_type   VARCHAR(100) NOT NULL," \
                        "office_name   VARCHAR(100) NOT NULL};"
        return create_office

    @staticmethod
    def create_parties_table():
        create_parties = "CREATE TABLE parties{" \
                         "_id         SERIAL  PRIMARY KEY NOT NULL," \
                         "party_name  VARCHAR(50)   NOT NULL," \
                         "hq_address  VARCHAR(100)  NOT NULL," \
                         "logo_url    VARCHAR(200)  NOT NULL};"
        return create_parties

    @staticmethod
    def create_votes_table():
        create_votes = "CREATE TABLE votes{" \
                       " _id          SERIAL  PRIMARY KEY NOT NULL," \
                       "created_on    DATE NOT NULL DEFAULT CURRENT_DATE," \
                       "created_by    INTEGER NOT NULL REFERENCES users(_id)  ," \
                       "office        INTEGER NOT NULL REFERENCES offices(_id), " \
                       "candidate     INTEGER NOT NULL REFERENCES  candidates(_id)};"
        return create_votes

    @staticmethod
    def create_candidates_table():
        create_candidates = "CREATE TABLE candidates{" \
                            " _id          SERIAL  PRIMARY KEY NOT NULL," \
                            "office        INTEGER NOT NULL REFERENCES offices(_id) ," \
                            "party         INTEGER NOT NULL REFERENCES parties(_id)  ," \
                            "candidate     INTEGER NOT NULL REFERENCES  users(_id)};"
        return create_candidates

    @classmethod
    def create_all_tables(cls):
        return cls.create_candidates_table().join(cls.create_office_table()).join(cls.create_parties_table()).join(
            cls.create_petition_table()).join(cls.create_votes_table()).join(cls.create_user_table())


class DropTables:

    def drop_user_table(self):
        pass

    def drop_petition_table(self):
        pass

    def drop_office_table(self):
        pass

    def drop_parties_table(self):
        pass

    def drop_votes_table(self):
        pass

    @classmethod
    def drop_all_tables(cls):
        pass
