########
#
# Django
#
########

DEBUG = True
SECRET_KEY = 'django-insecure-$eodx2ilnb*djkahfguiwegbwelgbnajl*u$qkt7j-b)7t1iq'
CSRF_TRUSTED_ORIGINS = []
ALLOWED_HOSTS = ["127.0.0.1"]
INTERNAL_IPS = ["127.0.0.1"]
NAME_SYSTEM = "ShariX"
API_URL = 'http://127.0.0.1:8000'

########
#
# Database
#
########

DB_NAME = None
DB_USER = None
DB_PASSWORD = None
DB_HOST = None
DB_PORT = 5432

########
#
# Email
#
########

EMAIL_HOST = None
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
DEFAULT_FROM_EMAIL = None

########
#
# Gunicorn
#
########

BIND = "127.0.0.1:8000"

########
#
# ejabber
#
########

EJ_PROTOCOL = "http"
EJ_IP = "10.0.20.9"
EJ_PORT = "5280"
EJ_URL = EJ_PROTOCOL + "://" + EJ_IP + ":" + EJ_PORT + "/" + "api/"
EJ_SERVICE = "chat.ej.sharix-app.org"
EJ_HOST = "ej.sharix-app.org"

# Service name that is used in generating ejabber rooms
WEBSERVICE_NAME = "open" 
