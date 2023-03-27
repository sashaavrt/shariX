#Create file config.py with this setting or rename this file to config.py

#BASE
DEBUG=True
SECRET_KEY='secret-key(absolutely any character)'
ALLOWED_HOSTS = ['127.0.0.1']
CSRF_TRUSTED_ORIGINS = []

#DATABSE
DB_NAME=None
DB_USER=None
DB_PASSWORD=None
DB_HOST=None

#GUNICORN
BIND = "127.0.0.1:8000"
WORKERS = 2
THREADS = 4

#STATIC
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "SharixAdmin/static/", BASE_DIR / "tickets/static/"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")