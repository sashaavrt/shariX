#!/bin/bash
git clone -b unstable http://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module http://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
python3 -m venv webapp-base
source webapp-base/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
#python3 manage.py makemigrations
#python3 manage.py migrate
#python3 manage.py collectstatic
#python3 manage.py createsuperuser
deactivate
