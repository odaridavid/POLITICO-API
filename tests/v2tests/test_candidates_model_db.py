from . import BaseTestCase
from api.v2.models.candidate import CandidateModel


class CandidatesModelTestCase(BaseTestCase):
    def test_candidate_registers_successfully(self):
        self.party.create_party()
        self.office.create_office()
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        candidate_info = self.candidate.register_candidate()
        self.assertEqual('David', candidate_info[0][2])

    def test_candidate_non_existent_cant_register(self):
        candidate = CandidateModel(1, 0, 0).register_candidate()
        self.assertEqual(candidate, 'Candidate Conflict')

    def test_candidate_cant_register_more_than_once(self):
        self.party.create_party()
        self.office.create_office()
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        self.candidate.register_candidate()
        response = self.candidate.register_candidate()
        self.assertEqual('Candidate Conflict', response)
