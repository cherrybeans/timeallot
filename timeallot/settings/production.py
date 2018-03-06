from .base import *

PRODUCTION = env('PRODUCTION')
DEBUG = False

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('HOST'),
        'PORT': '5490',
    }
}