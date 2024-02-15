#!/bin/bash

#cd <path to project>

source venv/Scripts/activate

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic -l --noinput

gunicorn core.wsgi:application -c core/gunicorn.py