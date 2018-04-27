import os

from .base import INSTALLED_APPS, ROOT_URLCONF

DEBUG = False
SECRET_KEY = 'secretkeythatisnotsosecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timeallot',
        'USER': 'timeallot',
        'PASSWORD': 'timeallot',
        'HOST': os.environ.get('DATABASE') or 'localhost',  # tox sends in DATABASE
        'PORT': os.environ.get('DATABASE') or '5490'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'user.TimerUser'
