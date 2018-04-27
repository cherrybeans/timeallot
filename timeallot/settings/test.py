import os

from .base import INSTALLED_APPS

DEBUG = False
SECRET_KEY = 'secretkeythatisnotsosecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE') or '127.0.0.1',  # tox sends in DATABASE
        'NAME': 'timeallot',
        'USER': 'timeallot'
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += []

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'user.TimerUser'
