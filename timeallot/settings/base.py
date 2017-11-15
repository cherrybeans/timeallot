"""
Django base settings for timeallot project.

Generated by 'django-admin startproject' using Django 1.11.7.
"""

import environ


### Overview ###
# GENERAL CONFIGURATION
# SECRET KEY
# APP CONFIGURATION
# DATABASE CONFIGURATION
# AUTHENTICATION CONFIGURATION
# EMAIL CONFIGURATION
# MIDDLEWARE CONFIGURATION
# TEMPLATE CONFIGURATION
# MANAGER CONFIGURATION
# INTERNATIONALIZATION
# URL CONFIGURATION
# PASSWORD VALIDATION
# STATIC FILES CONFIGURATION
# MEDIA FILES CONFIGURATION


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 2  # (timeallot/settings/base.py - 2 = timeallot/)
APPS_DIR = ROOT_DIR.path('apps/')
PUBLIC_ROOT = ROOT_DIR.path('public/')

env = environ.Env()
env.read_env()
# SECRET KEY
# ------------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'rest_framework',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    'utils',
    'timeallot.apps.user',
    'timeallot.apps.timer'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Uses django-environ to accept uri format
DATABASES = {
    'default': env.db()  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
# Select the correct user model
AUTH_USER_MODEL = 'user.TimerUser'


# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
# Email address that error messages come from.
SERVER_EMAIL = env('SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = '[timeallot] '
EMAIL_CONFIG = env.email('EMAIL_URL')
vars().update(EMAIL_CONFIG)


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = env('ADMINS')

MANAGERS = ADMINS


# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False


# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'timeallot.urls'

WSGI_APPLICATION = 'timeallot.wsgi.application'

# Location of root django.contrib.admin URL, use {% raw %}{% url 'admin:index' %}{% endraw %}
# ADMIN_URL = r'^admin/'


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
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


# # STATIC FILE CONFIGURATION
# # ------------------------------------------------------------------------------
STATIC_ROOT = str(PUBLIC_ROOT('static'))
STATIC_URL = '/static/'


STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(PUBLIC_ROOT('media'))
MEDIA_URL = '/media/'
