#!/bin/bash
git clone -b unstable https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
git clone -b webinterface https://git.sharix-app.org/ShariX_Open/sharix-open-webadmin.git SharixAdmin/templates/SharixAdmin
git clone -b master https://git.sharix-app.org/ShariX_Open/sharix-open-local.git openlocal
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
deactivate
