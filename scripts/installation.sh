#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 insall flask-mysqldb
source ~/.bashrc
python3 app.py