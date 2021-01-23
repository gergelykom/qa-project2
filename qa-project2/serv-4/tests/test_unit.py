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
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pasta' , 'qran' : '1800'})
        
        self.assertEqual(b"Congratulations, you just destroyed the Universe!", response.data)

    def test_whatudone3(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'burger' , 'qran' : '1800'})
        
        self.assertEqual(b"You just aided the emergence of intelligent sushi!", response.data)

    def test_whatudone4(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'burger' , 'qran' : '2400'})
        
        self.assertEqual(b"You just helped humanity to achieve techonological singularity!", response.data)

    def test_whatudone5(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pizza' , 'qran' : '1800'})
        
        self.assertEqual(b"You will get a hearthburn!", response.data)

     def test_whatudone6(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pizza' , 'qran' : '2400'})
        
        self.assertEqual(b"You will cause doplhins to take over the Earth!", response.data)

    def test_whatudone7(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pbj' , 'qran' : '1800'})
        
        self.assertEqual(b"You will cause crocs to be mandatory at fashion shows!", response.data)

    def test_whatudone8(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'pbj' , 'qran' : '2400'})
        
        self.assertEqual(b"Your actions will start a war with a K3 civilisation!", response.data)
        
        

