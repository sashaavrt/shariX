from pathlib import Path
import os
from core.db_settings import *
from core.api_settings import *
from core.tickets_mail_settings import *
from core.jazzmin_settings import *
import core.config as conf
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = conf.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf.DEBUG

ALLOWED_HOSTS = conf.ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = conf.CSRF_TRUSTED_ORIGINS

# Application definition
INSTALLED_APPS = [
    'design_template',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SharixAdmin.apps.SharixadminConfig',
    'tickets.apps.ticketsConfig',
    'metaservicesynced.apps.MetaservicesyncedConfig',
    'webservice_running.apps.WebserviceRunningConfig',
    'django_tables2',
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.admindocs",
    "django_extensions",
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'schema_graph',
    'drf_yasg',
    'django_spaghetti',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
]

ROOT_URLCONF = 'core.urls'

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_SECURITY_WARN_AFTER = 5
#SESSION_SECURITY_EXPIRE_AFTER = 12
INTERNAL_IPS = [
    '127.0.0.1',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "design_template.context_processors.get_name_system",
            ],
            'libraries': {
                'custom_tags':'tickets.template_tags.custom_tags'
            }
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "SharixAdmin/static/", BASE_DIR / "tickets/static/"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# Uploaded media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'SharixAdmin.SharixUser'

#Name System
NAME_SYSTEM = 'Sharix'

