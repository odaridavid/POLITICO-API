import unittest
# Imports create app function to set testing config
from run import create_app
# from api.db_conn import execute_drop_queries
from api.v2.models.user_model import UserModelDb
from api.v2.models.office_model import OfficesModelDb
from api.v2.models.candidate_model import CandidateModel
from api.v2.models.votes_model import VoteModel
from api.db_conn import create_tables, drop_tables, close_connection
from api.v2.models.parties_model import PartiesModelDb
import json


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        drop_tables()
        create_tables()
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.user = UserModelDb()
        self.user_invalid = UserModelDb()
        self.office = OfficesModelDb({"type": "Transport", "name": "Permernent Secretary"})
        self.office_invalid = OfficesModelDb({"type": "Transport", "name": ""})
        self.party = PartiesModelDb(
            {
                "name": "Party Name",
                "hqAddress": "Address",
                "logoUrl": "www.some.url.to.my.picture"
            })
        self.party_invalid = PartiesModelDb(
            {
                "name": "",
                "hqAddress": "A",
                "logoUrl": "www.some.url.to.my.picture"
            })
        self.candidate = CandidateModel(1, 1, 1)
        self.vote = VoteModel(office_id=1, candidate_id=1, user_id=1)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        drop_tables()
        close_connection()

    def generate_token(self):
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Kiddy",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "odari@kiddy.com",
            "phoneNumber": "0717453455",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": 0
        }))
        response = self.client.post('/api/v2/auth/login', data=json.dumps({
            "email": "odari@kiddy.com",
            "password": "1wwjdje3qr"
        }))
        # To access a jwt_required protected view,send in the JWT with the request
        auth_header = {'Authorization': 'Bearer {}'.format(response.json['token'])}
        return auth_header

    def generate_token_admin(self):
        self.client.post('api/v2/auth/signup', data=json.dumps({
            "firstname": "Admin",
            "lastname": "Odari",
            "othername": "Kiribwa",
            "email": "admin@theadmin.com",
            "phoneNumber": "0717453455",
            "passportUrl": "www.googledrive.com/pics?v=jejfek",
            "password": "1wwjdje3qr",
            "isAdmin": "t"
        }))
        response = self.client.post('/api/v2/auth/login', data=json.dumps({
            "email": "admin@theadmin.com",
            "password": "1wwjdje3qr"
        }))
        # To access a jwt_required protected view,send in the JWT with the request
        auth_header = {'Authorization': 'Bearer {}'.format(response.json['token'])}
        return auth_header
