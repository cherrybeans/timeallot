from .base import *
import raven
import os

DEBUG = env('DEBUG')
PRODUCTION = env('PRODUCTION')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# SECRET KEY
# ------------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ


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

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',

]

CODE_DIR = environ.Path(__file__) - 3

RAVEN_CONFIG = {
    'dsn': 'https://4c625294918e4875957099fee085d86b:fb491f76d56249309c4dcc8e713f6a5f@sentry.io/300508',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(CODE_DIR()),
}

MIDDLEWARE += [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]