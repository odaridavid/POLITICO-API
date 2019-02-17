from api.db_conn import db_connect
from werkzeug.security import generate_password_hash
import psycopg2


class UserModelDb:
    def __init__(self, user):
        # Setup connection to db
        self.db_conn = db_connect()
        # User object being worked on
        self.user = user

    def user_sign_up(self):
        firstname = self.user['firstname']
        lastname = self.user['lastname']
        othername = self.user['othername']
        email = self.user['email']
        phone_number = self.user['phoneNumber']
        passport_url = self.user['passportUrl']
        is_admin = self.user['isAdmin']
        # Hash and salt Password -Salting adding random data to the input of a hash function to guarantee a unique output,
        password = generate_password_hash(self.user['password'])
        # Add User to table
        query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,passport_url,pass,is_admin) " \
                "VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(firstname, lastname, othername, email,
                                                                          phone_number, passport_url, password,
                                                                          is_admin)

        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query)
            self.db_conn.commit()
            return firstname
        except psycopg2.ProgrammingError:
            # if the previous call to execute did not produce any result set or no call was issued yet.
            return 'Database Error'
        except psycopg2.IntegrityError:
            return 'User Exists'
