from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app
import json


class TestBase(TestCase):
    def create_app(self):
       

        return app

  
#test all
class TestResponse(TestBase):

    

    def test_whatudone(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'paella' , 'qran' : '2400'})


        self.assertEqual(b"You will cause the moon to leave Earth's orbit!", response.data)
        
    def test_whatudone2(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'paella' , 'qran' : '1600'})


        self.assertEqual(b"You will make siesta mandatory!", response.data)

    def test_whatudone3(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'stir-fry' , 'qran' : '1600'})
        
        
        self.assertEqual(b"A goose will be elected as president of the United States!", response.data)

    def test_whatudone4(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'stir-fry' , 'qran' : '2400'})
        
        self.assertEqual(b"You will make world-peace happen!", response.data)

    def test_whatudone5(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'lasagne' , 'qran' : '1600'})
        
        self.assertEqual(b"You will cause a massive (literal) headache for someone!", response.data)

    def test_whatudone6(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'lasagne' , 'qran' : '2400'})
        
        self.assertEqual(b"Your meal will cause turnips to rise and enslave humanity!", response.data)

    def test_whatudone7(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'korean style mapo tofu' , 'qran' : '1600'})
        
        self.assertEqual(b"You will cause number 11 to be removed!", response.data)

    def test_whatudone8(self):
        response = self.client.post(url_for('whatudone'), json={ 'meal' : 'korean style mapo tofu' , 'qran' : '2400'})
        
        self.assertEqual(b"Your actions will cut infinity into half!", response.data)
        
        

