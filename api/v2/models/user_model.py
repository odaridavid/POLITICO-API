from api.db_conn import db_connect
from werkzeug.security import generate_password_hash
import psycopg2
from api.validator import UserValidator


class UserModelDb:
    def __init__(self, user):
        # Setup connection to db
        self.db_conn = db_connect()
        # User object being worked on
        self.user = user

    def user_sign_up(self):
        validated_user = UserValidator(self.user).all_checks()
        if 'Invalid' in validated_user:
            return 'Invalid Data'
        firstname = validated_user['firstname']
        lastname = validated_user['lastname']
        othername = validated_user['othername']
        email = validated_user['email']
        phone_number = validated_user['phoneNumber']
        passport_url = validated_user['passportUrl']
        is_admin = self.user['isAdmin']
        # Check admin else default to 0
        if is_admin == 0 or is_admin == 1 or is_admin == 't' or is_admin == 'f':
            admin_status = is_admin
        else:
            admin_status = 0
        # Hash and salt Password -Salting adding random data to the input of a hash function to guarantee a unique output,
        password = generate_password_hash(validated_user['password'])
        # Add User to table
        query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,passport_url,pass,is_admin) " \
                "VALUES('{}','{}','{}','{}','{}','{}','{}','{}');".format(firstname, lastname, othername, email,
                                                                          phone_number, passport_url, password,
                                                                          admin_status)

        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query)
            self.db_conn.commit()
            return firstname
        except psycopg2.IntegrityError:
            return 'User Exists'
