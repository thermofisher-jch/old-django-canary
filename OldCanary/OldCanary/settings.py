"""
Django settings for IonInspector project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "flejwqfh@#Q@$J#Fjnj3nfaf90b3723/qi329j3kn.j#WML@KN#!nqeblijv"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", "" if DEBUG else "localhost,127.0.0.1"
).split(",")
ALLOWED_HOSTS = [] if not any(ALLOWED_HOSTS) else ALLOWED_HOSTS

# Application definition
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Things.apps.ThingsConfig",
    "crispy_forms",
    "django_filters",
    "django_tables2",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "OldCanary.urls"
WSGI_APPLICATION = "OldCanary.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# HOST Note!!! this is defined by the name of the docker container which is running postgres
DATABASES = {
    "default": {
        "NAME": "old-canary",
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": os.getenv("DATABASE_USERNAME", "canary"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "tweet"),
        "HOST": "postgres",
        "PORT": "5432",
    }
}

# Cannot use sqlite with array field
# if 'test' in sys.argv or 'test_coverage' in sys.argv:  # Covers regular testing and django-coverage
#    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG" if DEBUG else "INFO",
            "class": "logging.StreamHandler"
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "DEBUG" if DEBUG else "INFO",
            "propagate": True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


TEMPLATES = [
    {
        "NAME": "Inspector",
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MEDIA_ROOT = "/var/lib/inspector/media/"
MEDIA_URL = "/media/"

CELERY_IGNORE_RESULT = False
CELERY_TASK_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["pickle", "json"]
CELERY_RESULT_BACKEND = "rpc"
CELERY_RESULT_SERIALIZER = "pickle"
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))


VERSION = "1.8.1-rc.2"
try:
    # Allows contextual override of displayed version tag
    with open("/var/lib/inspector/version", "r") as fd:
        VERSION = fd.read()
except IOError as e:
    pass

RAVEN_CONFIG = {
    "dsn": "http://d8a6a72730684575afc834c95ebbdc60:1e5b396140654efd9b3361401f530204@sentry.itw//11",
    "release": VERSION,
}

try:
    from local_version import *
except ImportError:
    pass

try:
    from local_settings import *
except ImportError:
    pass
