from . import BaseTestCase


class PartiesEndpointsTestCase(BaseTestCase):
    def test_create_political_party(self):
        """Tests POST Http method request on /parties endpoint"""
        pass

    def test_create_political_party_bad_request(self):
        """Tests malformed POST Http method request on /parties endpoint"""
        pass

    def test_edit_political_party(self):
        """Tests PATCH Http method request on /parties/{:id}/name endpoint"""
        pass

    def test_edit_political_party_bad_request(self):
        """Tests malformed PATCH Http method request on /parties/{:id}/name endpoint"""
        pass

    def test_delete_political_party(self):
        """Tests DELETE Http method request on /parties/{:id} endpoint"""
        pass

    def test_delete_political_party_not_found(self):
        """"Tests malformed DELETE Http method request on /parties/{:id} endpoint"""
        pass

    def test_view_political_party(self):
        """Tests GET Http method request on /parties/{:id} endpoint"""
        pass

    def test_view_political_party_not_found(self):
        """Tests malformed GET Http method request on /parties/{:id} endpoint"""
        pass

    def test_view_all_political_parties(self):
        """Tests GET Http method request on /parties/ endpoint"""
        pass

    def test_view_all_political_parties_bad_request(self):
        """Tests malformed GET Http method request on /parties/ endpoint"""
        pass
