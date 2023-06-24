#!/bin/bash
cd /root/sharix-open-webapp-base
source env/bin/activate
python manage.py collectstatic --no-input