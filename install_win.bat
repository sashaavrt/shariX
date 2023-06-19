@echo off
cd design_template/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git
git checkout unstable
cd ..
cd tickets/
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git 
git checkout unstable
cd ..
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
python -m venv env
.\env\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver