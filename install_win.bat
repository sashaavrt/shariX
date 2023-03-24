@echo off
git clone -b tickets_module http://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module http://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
python -m venv env
.\env\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
