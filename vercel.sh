#!/bin/bash

echo 'starting build sequence';
apt install -y python3-pip;
pip install -r requirements.txt;
python3 manage.py makemigrations;
python3 manage.py migrate;
echo 'build Complete';
echo 'starting deployment sequence';
python3 manage.py runserver;
echo 'deployment complete';