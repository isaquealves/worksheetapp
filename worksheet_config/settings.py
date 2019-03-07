"""
Django settings for worksheet project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kbawwoyw3fw6(d%4cjp26k+*ru7o4nnzt=z4vkc*omas#4!jyr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ***REMOVED******REMOVED***


# Application definition

INSTALLED_APPS = ***REMOVED***
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'worksheet',


***REMOVED***

MIDDLEWARE = ***REMOVED***
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
***REMOVED***

ROOT_URLCONF = 'worksheet_config.urls'

TEMPLATES = ***REMOVED***
    ***REMOVED***
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ***REMOVED******REMOVED***,
        'APP_DIRS': True,
        'OPTIONS': ***REMOVED***
            'context_processors': ***REMOVED***
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ***REMOVED***,
    ***REMOVED***,
***REMOVED***,
***REMOVED***

WSGI_APPLICATION = 'worksheet_config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = ***REMOVED***
    'default': ***REMOVED***
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
***REMOVED***
***REMOVED***

DATABASES***REMOVED***'default'***REMOVED*** = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = ***REMOVED***
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
***REMOVED***,
    ***REMOVED***
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
***REMOVED***,
***REMOVED***
LOGIN_URL = 'worksheet_login'
LOGIN_REDIRECT_URL = 'transaction_list'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
