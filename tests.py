import unittest
from beckton import app, db
from mongoengine import connect
import os

class Tests(unittest.TestCase):

    def _drop_database(self):
        mongo_settings =  app.config['MONGODB_SETTINGS']
        db = connect(mongo_settings['DB'])
        db.drop_database(mongo_settings['DB'])

    def setUp(self):
        self.app = app.test_client()
        self._drop_database()

    def tearDown(self):
        self._drop_database()

    def test_alive(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'

    def test_commit_invalid(self):

        rv = self.app.post('/', data={})
        assert rv.status == '200 OK'
        assert "You need to enter your name" in rv.data
        assert "You need to enter a valid mobile phone number" in rv.data
        assert "You need to agree" in rv.data

        #test name
        rv = self.app.post('/', data={"name": "William Shu"})
        assert rv.status == '200 OK'
        assert "You need to enter your name" not in rv.data
        assert "You need to enter a valid mobile phone number" in rv.data
        assert "You need to agree" in rv.data

        #test phone
        rv = self.app.post('/', data={"mobile_number": "07877666555"})
        assert rv.status == '200 OK'
        assert "You need to enter your name" in rv.data
        assert "You need to enter a valid mobile phone number" not in rv.data
        assert "You need to agree" in rv.data

        #test agreed
        rv = self.app.post('/', data={"agree": 1})
        assert rv.status == '200 OK'
        assert "You need to enter your name" in rv.data
        assert "You need to enter a valid mobile phone number" in rv.data
        assert "You need to agree" not in rv.data

    def test_commit_valid(self):
        rv = self.app.post('/', data= {"name": "Greg Orlowski", "mobile_number": "07877666555", "agree": 1}, follow_redirects=True)
        assert rv.status == '200 OK'
        assert "You are the first person to agree. The target is %d people" % app.config['CONDITION_TARGET'] in rv.data

    def test_commit_cannot_signup_twice(self):
        rv = self.app.post('/', data= {"name": "Greg Orlowski", "mobile_number": "07877666555", "agree": 1}, follow_redirects=True)
        assert rv.status == '200 OK'
        assert "You are the first person to agree. The target is %d people" % app.config['CONDITION_TARGET'] in rv.data

        rv = self.app.post('/', data= {"name": "Greg Orlowski", "mobile_number": "07877666555", "agree": 1}, follow_redirects=True)
        assert rv.status == '200 OK'
        assert "Someone has already signed up with that phone number" in rv.data

if __name__ == '__main__':
    unittest.main()