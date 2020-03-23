#!/bin/bash
echo "Installing Dependencies..."
sudo apt update -y -qq
sudo apt install python3 -y -qq
sudo apt install python3-pip -y -qq
sudo apt install python3-venv -y -qq
sudo apt-get install libmysqlclient-dev -y -qq
sudo apt-get install gunicorn -y -qq
python3 -m venv venv
