#!/bin/bash
cd design_template/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git
git checkout unstable
cd ..
cd tickets/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git 
git checkout unstable
git cd ..
cd metaservicesynced/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git
git checkout unstable
cd ..
cd sharix-open-config/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-config.git
git checkout unstable
cd ..
cd webservice_running/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git
git checkout unstable
cd .. 
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
