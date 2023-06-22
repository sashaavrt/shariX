#!/bin/bash
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git design_template
cd design_template
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets 
cd tickets
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
cd metaservicesynced
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-config.git sharix-open-config
cd sharix-open-config
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git webservice_running
cd webservice_running
git checkout unstable
cd .. 
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
#python3 manage.py createsuperuser
deactivate
chmod -x update_unix.sh install_unix.sh bin/webuser.sh
chmod u+x update_unix.sh install_unix.sh bin/webuser.sh
cp sharix-open-config/sharix_open.service /etc/systemd/system/
