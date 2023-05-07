#!/bin/bash
cd /root/sharix-open-webapp-base
exec /root/sharix-open-webapp-base/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
