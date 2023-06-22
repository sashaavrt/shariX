#!/bin/bash
#cd /path/to/project
cd /root/sharix-open-webapp-base/
#exec /path/to/project/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
exec /root/sharix-open-webapp-base/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
