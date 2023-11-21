import os

from pathlib import Path

from django.contrib.messages import constants as message_constants
from django.utils.translation import gettext_lazy as _

import core.settings_vars as sv


########
#
# Django
#
########

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = sv.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = sv.DEBUG
CSRF_TRUSTED_ORIGINS = sv.CSRF_TRUSTED_ORIGINS
ALLOWED_HOSTS = sv.ALLOWED_HOSTS 
INTERNAL_IPS = sv.INTERNAL_IPS

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
    'tickets.apps.TicketsConfig',
    'metaservicesynced.apps.MetaservicesyncedConfig',
    'webservice_running.apps.WebserviceRunningConfig',
    'django_tables2',
    'schema_graph',
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django_extensions",
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',
    'django_spaghetti',
    'debug_toolbar',
    'ckeditor',
    'landing.apps.LandingConfig',
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
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "core.urls"

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SECURITY_WARN_AFTER = 5
SESSION_SECURITY_EXPIRE_AFTER = 12

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "design_template.context_processors.get_name_system",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if sv.DB_NAME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': sv.DB_NAME,
            'USER': sv.DB_USER,
            'PASSWORD': sv.DB_PASSWORD,
            'HOST': sv.DB_HOST,
            'PORT': sv.DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'ru'
USE_TZ = True
TIME_ZONE = 'Europe/Moscow'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Uploaded media
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Without this, uploaded files > 4MB end up with perm 0600, unreadable by web server process
FILE_UPLOAD_PERMISSIONS = 0o644

# Override CSS class for the ERROR tag level to match Bootstrap class name
MESSAGE_TAGS = {message_constants.ERROR: "danger"}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'SharixAdmin.SharixUser'

NAME_SYSTEM = sv.NAME_SYSTEM

########
#
# Jazzmin
#
########

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "ShariX Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "ShariX Platform",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "ShariX Platform",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "SharixAdmin/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the ShariX Admin",

    # Copyright on the footer
    "copyright": "Acme Library Ltd",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["SharixAdmin.SharixUser"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Главная",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        #{"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "SharixAdmin.SharixUser"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "tickets"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "SharixAdmin.SharixUser"}
    # ],

    # #############
    # # Side Menu #
    # #############

    # # Whether to display the side menu
    # "show_sidebar": True,

    # # Whether to aut expand the menu
    # "navigation_expanded": True,

    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": [],

    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],

    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # #"order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "tickets": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["tickets.view_book"]
    #     }]
    # },

    # # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "SharixAdmin": "fas fa-users-cog",
        "SharixAdmin.SharixUser": "fas fa-user",
        "tickets.Task": "fas fa-check",
        "tickets.TaskList": "fas fa-list",
        "tickets.Comment": "fas fa-comment",
        "tickets.Attachment": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    # # "default_icon_parents": "fas fa-chevron-circle-right",
    # # "default_icon_children": "fas fa-circle",

    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    # "related_modal_active": False,

    # #############
    # # UI Tweaks #
    # #############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
        "custom_css": None,
        "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
        "use_google_fonts_cdn": True,
    # # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    #"changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    #"changeform_format_overrides": {"SharixAdmin.SharixUser": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    #"language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-light",
    "accent": "accent-navy",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False
}

########
#
# API
#
########

API_URL = sv.API_URL

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_RENDERER_CLASSES':[
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SPAGHETTI_SAUCE = {
    'apps': ['auth', 'SharixAdmin', 
                'tickets', 'admin', 
                'flatpages', 'sessions', 'sites', 'metaservicesynced'],
    'show_fields': False,
    'show_proxy':True,
}

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}
