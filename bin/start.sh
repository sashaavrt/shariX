#!/bin/bash

#cd <path to project>

venv\bin\activate

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic -l --noinput

gunicorn core.wsgi:application -c core/gunicorn.py