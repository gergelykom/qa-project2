from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app
import json


class TestBase(TestCase):
    def create_app(self):
       

        return app

  

class TestResponse(TestBase):

    

    def test_whatudone(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pasta' , 'qran' : '2400'})
       
        
        self.assertEqual(b"You will roll 6 nat20's in a row!", response.data)
        
    def test_whatudone2(self):
        response = self.client.post(url_fot('whatudone'), json={ 'meal' : 'pasta' , 'qran' : '1800'})
        
        self.assertEqual(b"Congratulations, you just destroyed the Universe!", response.data)
        
        

