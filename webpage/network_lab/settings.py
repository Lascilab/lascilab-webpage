"""
Django settings for network_lab project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if socket.gethostname() == "produccion": 
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = True
else: 
    SECRET_KEY = 'x!edk(ippl&a+1mjo0uwqaq-%jz$oehvi9udpki0je)n&ujq+p'
    DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'network_lab.apps.activities',
    'network_lab.apps.courses',
    'network_lab.apps.index',
    'network_lab.apps.members',
    'network_lab.apps.projects',
    'network_lab.apps.research',
    'network_lab.apps.resources',
    'network_lab.apps.thesis',

    # Third Party apps
    'base',
    'network_lab.apps.blog_engine',
    'network_lab.apps.simple_auth',
    'network_lab.apps.static_html_engine',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'network_lab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'network_lab.apps.blog_engine.context_processors.blog_engine_urls',
                'network_lab.apps.blog_engine.context_processors.site_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'network_lab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if socket.gethostname() == "produccion": 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASS'],
            'HOST': os.environ['DB_SERVICE'],
            'PORT': os.environ['DB_PORT']
        }
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.environ['DB_NAME'],
#        'USER': os.environ['DB_USER'],
#        'PASSWORD': os.environ['DB_PASS'],
#        'HOST': os.environ['DB_SERVICE'],
#        'PORT': os.environ['DB_PORT']
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")

if socket.gethostname() == "produccion": 
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = '/media/'
else: 
    MEDIA_ROOT = os.path.join(BASE_DIR, "static", "img")
