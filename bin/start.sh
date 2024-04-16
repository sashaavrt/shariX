#!/bin/bash

cd /root/sharix-assist-webapp-base/

source venv/bin/activate

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic -l --noinput

gunicorn core.wsgi:application -c core/gunicorn.py
