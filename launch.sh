#!/bin/bash

# Setting up the environment 
#sudo apt-get install python3
#sudo apt-get install python3-pip -y
#sudo apt-get install python3-venv -y
#pip3 install -U flask
#pip3 --version
#source /home/Admin/projects/web_design/venv/bin/activate


gunicorn --workers=4 --bind=0.0.0.0:5000 app:app

