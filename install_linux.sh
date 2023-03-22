#!/bin/sh

git clone -b tickets_module http://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git tickets

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver