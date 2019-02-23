from . import BaseTestCase
from api.v2.models.votes import VoteModel


class VotesModelTestCase(BaseTestCase):
    def test_user_can_vote_successfully(self):
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
        vote = self.vote.vote()
        self.assertEqual(vote, [(1, 1, 1)])

    def test_user_cant_vote_twice_same_office(self):
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
        self.vote.vote()
        vote_again = self.vote.vote()
        self.assertEqual('Vote Conflict', vote_again)

    def test_user_cant_vote_for_non_existent_items(self):
        vote = VoteModel(0, 0, 0).vote()
        self.assertEqual(vote, 'Vote Conflict')
