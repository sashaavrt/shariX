@echo off
git clone -b unstable http://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module http://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
git clone -b webinterface https://git.sharix-app.org/ShariX_Open/sharix-open-webadmin.git SharixAdmin/templates/SharixAdmin
git clone -b master https://git.sharix-app.org/ShariX_Open/sharix-open-local.git openlocal
python -m venv env
.\env\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
