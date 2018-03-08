"""
Local development settings for timeallot project.
"""

from .base import *

### Overview ###
# DEBUG
# GENERAL CONFIGURATION
# APP CONFIGURATION
# DATABASE CONFIGURATION


# GENERAL CONFIGURATION
#  ------------------------------------------------------------------------------

DEBUG = True
DEVELOPMENT = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1', ]

SERVER_URL = env('SERVER_URL')
FRONTEND_URL = env('FRONTEND_URL')

# SECRET KEY
# ------------------------------------------------------------------------------
SECRET_KEY = 'secretkeythatisnotsosecret'


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timeallot',
        'USER': 'timeallot',
        'PASSWORD': 'timeallot',
        'HOST': 'localhost',
        'PORT': '5490',
    }
}


# APP CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# DEBUG-TOOLBAR CONFIGURATION
# ------------------------------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
SERVER_EMAIL = env('SERVER_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

