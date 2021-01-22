#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip


cd serv-1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml 
deactivate
cd ..


cd serv-2
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml 
deactivate
cd ..


cd serv-3
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml 
deactivate
cd ..


cd serv-4
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=application --cov-report xml 
deactivate
cd ..