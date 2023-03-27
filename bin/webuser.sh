#!/bin/bash
cd /path/to/project
exec /path/to/project/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
