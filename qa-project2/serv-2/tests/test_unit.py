from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
       

        return app

  

class TestResponse(TestBase):

    

    def test_qran(self):
        with patch("random.choice") as random:
            random.return_value = "4000"           
            response = self.client.get(url_for('get_qran'))
            self.assertEqual(b'4000', response.data)

        for _ in range(10):
            response = self.client.get(url_for('get_qran'))
            self.assertIn(response.data, [b"80", b"800", b"1600", b"2400", b"3200", b"4000"])