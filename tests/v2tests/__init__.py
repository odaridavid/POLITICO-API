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


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        drop_tables()
        create_tables()
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.user = UserModelDb(
            user={"firstname": "David",
                  "lastname": "Odari",
                  "othername": "Kiribwa",
                  "email": "odari@gmail.com",
                  "phoneNumber": "0717455945",
                  "passportUrl": "www.googledrive.com/pics?v=jejfek",
                  "password": "12we3e4r",
                  "isAdmin": 'f'
                  })
        self.user_invalid = UserModelDb(
            user={"firstname": "David",
                  "lastname": "Od",
                  "othername": "Kiribwa",
                  "email": "odari@mail.com",
                  "phoneNumber": "0717455945",
                  "passportUrl": "www.googledrive.com/pics?v=jejfek",
                  "password": "12we3e4r"
                  })
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

    def tearDown(self):
        drop_tables()
        close_connection()
