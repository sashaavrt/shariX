#!/bin/bash
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git 
git checkout unstable
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git
git checkout metasynced_module
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-local.git
git checkout unstable
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-config.git
git checkout unstable 
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git
git checkout unstable 
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
deactivate
cp conf/sharix_open.service /etc/systemd/system/
