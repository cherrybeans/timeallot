"""
Local development settings for timeallot project.
"""

from timeallot.settings.base import *

### Overview ###
# DEBUG
# GENERAL CONFIGURATION
# APP CONFIGURATION


# SECRET KEY
# ------------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
# TEMPLATE_DEBUG = DEBUG


# GENERAL CONFIGURATION
#  ------------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']

SERVER_URL = env('SERVER_URL')
FRONTEND_URL = env('FRONTEND_URL')

INTERNAL_IPS = '127.0.0.1'


# APP CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += []
