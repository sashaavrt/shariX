@echo off
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
python -m venv env
.\env\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver