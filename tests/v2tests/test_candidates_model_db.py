from . import BaseTestCase
from api.v2.models.candidate import CandidateModel


class CandidatesModelTestCase(BaseTestCase):
    def test_candidate_registers_successfully(self):
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.office.create_resource('office', {"type": "Transport", "name": "Permernent Secretary"})
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        candidate_info = self.candidate.register_candidate(1, 1, 1)
        self.assertEqual('David', candidate_info[0][2])

    def test_candidate_non_existent_cant_register(self):
        candidate = CandidateModel().register_candidate(1, 0, 0)
        self.assertEqual(candidate, 'Candidate Conflict')

    def test_candidate_cant_register_more_than_once(self):
        self.party.create_resource('party', {
            "name": "Party Name",
            "hqAddress": "Address",
            "logoUrl": "www.some.url.to.my.picture"
        })
        self.office.create_resource('office', {"type": "Transport", "name": "Permernent Secretary"})
        self.user.user_sign_up({"firstname": "David",
                                "lastname": "Odari",
                                "othername": "Kiribwa",
                                "email": "odari@gmail.com",
                                "phoneNumber": "0717455945",
                                "passportUrl": "www.googledrive.com/pics?v=jejfek",
                                "password": "12we3e4r",
                                "isAdmin": 'f'
                                })
        self.candidate.register_candidate(1, 1, 1)
        response = self.candidate.register_candidate(1, 1, 1)
        self.assertEqual('Candidate Conflict', response)
