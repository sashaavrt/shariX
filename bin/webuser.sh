#!/bin/bash
cd /root/sharix-webuser
source /root/sharix-webuser/webuser/bin/activate
exec python3 manage.py runserver 10.0.2.120:8001
