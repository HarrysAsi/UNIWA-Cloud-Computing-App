"""
Django settings for UniwaCloudExercises project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from .CONFIG import (
    DOMAIN_REGEX
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't#h)vc*^6p$(d@2f6(usd_&g^%-@7qt)hs6z$m4@c+dfv9!19q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

# Custom User Model
AUTH_USER_MODEL = 'user.CustomUser'

# Application definition

PREREQUISITE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.user',
    'apps.cloud',
    'apps.subject',
]

PACKAGES_APPS = [
    # Form package helper
    'corsheaders',
]

INSTALLED_APPS = PREREQUISITE_APPS + PROJECT_APPS + PACKAGES_APPS

ROOT_URLCONF = 'UniwaCloudExercises.urls'

MIDDLEWARE = [
    #     Cors Middleware needs to be on top
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # users can choose their language we use the locale middleware.
    'django.middleware.locale.LocaleMiddleware',
]

# TEMPLATE_DIRS = (
#     os.path.join(SETTINGS_PATH, 'templates'),
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'UniwaCloudExercises.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# File Permissions
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# specify the path of the directory and we access the media folder
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CORS CONFIGURATION
DOMAIN_REGEX = DOMAIN_REGEX

CORS_ORIGIN_REGEX_WHITELIST = [
    r"(https|http)://[\w\-]*.?" + DOMAIN_REGEX + ".(com|gr){1}.*",
]
if DEBUG:
    CORS_ORIGIN_REGEX_WHITELIST = [
        r"(https|http)://[\w\-]*.?" + DOMAIN_REGEX + ".(com|gr){1}.*",
        # Debug mode (localhost / 127.0.0.1)
        r"(https|http)://[\w\-\\.:]*\d.$",
    ]
