from .base import *

PRODUCTION = env('PRODUCTION')
DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timeallot',
        'USER': 'timeallot',
        'PASSWORD': 'timeallot',
        'HOST': "db",
        'PORT': '5432',
    }
}

SERVER_EMAIL = env('SERVER_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']
