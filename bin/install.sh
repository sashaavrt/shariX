#!/bin/bash

git clone -b master https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
git clone -b webinterface https://git.sharix-app.org/ShariX_Open/sharix-open-webadmin.git SharixAdmin/templates/SharixAdmin
git clone -b master https://git.sharix-app.org/ShariX_Open/sharix-open-config.git conf

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

if [ -f core/config.py ]; then
    echo "File config.py already created"
else
    cp core/_config.py core/config.py
    echo "File config.py was successfully created"
fi

python manage.py makemigrations SharixAdmin metaservicesynced tickets
python manage.py migrate
python manage.py collectstatic -l --no-input
python manage.py createsuperuser

#cp conf/sharix_open.service /etc/systemd/system/