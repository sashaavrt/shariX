git clone -b master http://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets
git clone -b metasynced_module http://git.sharix-app.org/ShariX_Open/sharix-open-backend.git metaservicesynced
git clone -b webinterface https://git.sharix-app.org/ShariX_Open/sharix-open-webadmin.git SharixAdmin/templates/SharixAdmin

python -m venv venv
.\venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

if exist core\config.py (
    echo File config.py already created
) else (
    copy core\_config.py core\config.py
    echo File config.py was successfully created
)

python manage.py makemigrations SharixAdmin metaservicesynced tickets
python manage.py migrate
python manage.py collectstatic -l --no-input
python manage.py createsuperuser
