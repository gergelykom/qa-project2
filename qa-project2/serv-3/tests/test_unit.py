from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app


class TestBase(TestCase):
    def create_app(self):
       

        return app

  

class TestResponse(TestBase):

    

    def test_meal(self):
        with patch("random.choice") as random:
            random.return_value = "paella"           
            response = self.client.get(url_for('get_meal'))
            self.assertEqual(b'paella', response.data)

        for _ in range(10):
            response = self.client.get(url_for('get_meal'))
            self.assertIn(response.data, [b"paella", b"stir-fry", b"lasagne", b"korean style mapo tofu"])
        