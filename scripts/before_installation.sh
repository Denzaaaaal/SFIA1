#!/bin/bash
echo "Installing Dependencies..."
sudo apt update -y -qq > /dev/null
sudo apt install python3 -y -qq > /dev/null
sudo apt install python3-pip -y -qq > /dev/null
sudo apt install python3-flask -y -qq > /dev/null
sudo apt install python3-venv -y -qq > /dev/null
sudo apt-get install libmysqlclient-dev -y -qq > /dev/null
# sudo apt-get install gunicorn -y -qq > /dev/null
python3 -m venv venv