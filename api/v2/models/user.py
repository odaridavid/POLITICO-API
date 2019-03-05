from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from api.validator import UserValidator
from flask_jwt_extended import create_access_token
from . import Model


class UserModelDb(Model):

    def user_sign_up(self, user):
        validated_user = UserValidator(user).all_checks()
        if 'Invalid' in validated_user:
            return 'Invalid Data'
        firstname = validated_user['firstname']
        lastname = validated_user['lastname']
        othername = validated_user['othername']
        email = validated_user['email']
        phone_number = validated_user['phoneNumber']
        passport_url = validated_user['passportUrl']
        is_admin = user['isAdmin']
        # Check admin else default to 0
        if is_admin == 't' or is_admin == 'f':
            admin_status = is_admin
        else:
            admin_status = 'f'
        # Hash and salt Password -Salting adding random data to the input of a hash function to guarantee a unique output,
        password = generate_password_hash(validated_user['password'])
        data = (firstname, lastname, othername, email, phone_number, passport_url, password, admin_status)
        query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,passport_url,pass,is_admin) " \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s) RETURNING _id;"

        try:
            cursor = self.db_conn.cursor()
            cursor.execute(query, data)
            self.db_conn.commit()
            user_row = cursor.fetchall()
            _id = user_row[0][0]
            access_token = create_access_token(identity=_id)
            return access_token
        except psycopg2.IntegrityError:
            return 'User Exists'

    def user_sign_in(self, user):
        email = user['email']
        password = user['password']
        query = """SELECT _id,pass FROM users WHERE email = %s;"""

        cursor = self.db_conn.cursor()
        # Execute function works with iterable
        cursor.execute(query, (email,))
        self.db_conn.commit()
        user_row = cursor.fetchall()
        if len(user_row) < 1:
            return 'Non Existent User'
        # Check passwords match
        _id = user_row[0][0]
        if check_password_hash(user_row[0][1], password):
            access_token = create_access_token(identity=_id)
            return access_token
        return 'Invalid'

    def get_user_by_id(self, _id):
        query = """SELECT * FROM users WHERE _id = %s;"""
        cursor = self.db_conn.cursor()
        # Execute function works with iterable
        cursor.execute(query, (_id,))
        self.db_conn.commit()
        user_row = cursor.fetchall()
        if user_row[0][8]:
            return 'Can Perform Operations'
        return 'Requires Admin Privilege'
