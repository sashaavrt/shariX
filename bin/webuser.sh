#!/bin/bash
cd /root/sharix-open-webapp-base
exec /root/sharix-open-webapp-base/webapp-base/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
