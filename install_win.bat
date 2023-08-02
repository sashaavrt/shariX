@echo off
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git design_template
cd design_template/
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
cd tickets/
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
cd metaservicesynced/
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-config.git sharix-open-config
cd sharix-open-config/
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git webservice_running
cd webservice_running/
git checkout unstable
cd ..
git clone https://git.sharix-app.org/ShariX_Open/sharix-open-landing.git landing
cd landing/
git checkout landing_module
cd ..
python -m venv env
.\env\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver