#!/bin/bash

source venv/bin/activate

pip3 install flask

pip3 install flask-mysqldb
pip3 install urllib
pip3 install pytest
pip3 install coverage
source ~/.bashrc
python3 app.py
