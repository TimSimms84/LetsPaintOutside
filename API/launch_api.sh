#!/usr/bin/env bash

# This script is used to setup the environment for the project.
# It is meant to be run from the root of the project.

# setup python
# sudo apt update
# sudo apt upgrade
# sudo apt install python3-pip
# sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 modify.py 
python3 setup_db.py
uvicorn app:app --reload
