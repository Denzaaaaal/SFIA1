#!/bin/bash

echo "Activating the virtual environment..."
source venv/bin/activate
echo "Installing pip dependencies..."
pip3 install flask
pip3 install flask-mysqldb
pip3 install urllib
pip3 install pytest
pip3 install coverage
source ~/.bashrc
echo "Starting application..."
# Uses python app to launch the web application
python3 app.py

# Uses Gunicorn to launch the application
# gunicorn --workers=4 --bind=0.0.0.0:5000 app:app
