from pathlib import Path
import os
import core.config as conf

BASE_DIR = Path(__file__).resolve().parent.parent
if conf.DB_NAME is None:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': conf.DB_NAME,
            'USER': conf.DB_USER,
            'PASSWORD': conf.DB_PASSWORD,
            'HOST': conf.DB_HOST,
            'PORT': '5432',
        }
    }

