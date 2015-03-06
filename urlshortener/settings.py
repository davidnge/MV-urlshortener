"""
Django settings for urlshortener project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname((__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2pm3!cbxogn^g$t!42&t-k7(p%^1m7=j2*18gze43=jyk#plyg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shortener',
    'crispy_forms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ROOT_URLCONF = 'urlshortener.urls'

WSGI_APPLICATION = 'urlshortener.wsgi.application'

BITLY_USER = 'davidnge'
BITLY_API_KEY = 'R_f5231f7a4063408e81202b9725a6c6fa'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6sibqnhk0ajhp',
        'USER': 'eaocqbtovogznf',
        'PASSWORD': '193zs5otP-aBlGSHGPY9OAPMLU',
        'HOST': 'ec2-50-19-249-214.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}




# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Static files (CSS, JavaScript, Images)

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
    )

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/




# Parse database configuration from $DATABASE_URL


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "root")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
    )

