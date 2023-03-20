"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iw+b1%p9&zw_+#gx+m&aw$gza2-_p6$03s3&4p+4kbd8%o0b_8'

if 'PYTHONPATH' in os.environ:
    # Debug = True
    Debug = False
    # Ensure the below line is set to the region where your elastic beanstalk is set up
    ALLOWED_HOSTS = ['.ap-southeast-2.elasticbeanstalk.com']
else:
    # SECURITY WARNING: don't run with debug turned on in production!
    # We need this to work in development environment but not on testing or production environments
    # We do not want to reveal errors in our server-side to the public in case if that happens
    DEBUG = True
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'storages', #for static files

    'myproject',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
            'default': {
                'ENGINE':'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

'''
if 'S3_BUCKET' in os.environ:

    AWS_STORAGE_BUCKET_NAME = 'sample-crud-bucket-cs204'
    AWS_S3_REGION_NAME = 'ap-southeast-2'

    print("DOES IT GET HERE???")

    # Ideally these keys must be stored inside environment properties of Beanstalk
    # and referenced as
    # AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
    # AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
    AWS_S3_ACCESS_KEY_ID = 'AKIAWT2NGT2X3SQ4VYGR'
    AWS_S3_SECRET_ACCESS_KEY = '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'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    print("AWS S3 CUSTOM DOMAIN IS: ")
    print(AWS_S3_CUSTOM_DOMAIN)

    AWS_S3_OBJECT_PARAMETERS = {
       'CacheControl': 'max-age=86400', #Cache lasts for 1 day
    }

    AWS_S3_FILE_OVERWRITE = False
    #AWS_DEFAULT_ACL = 'public-read'
    AWS_DEFAULT_ACL = None
    AWS_STATIC_FILES_LOCATION = 'static'
    STATICFILES_DIRS = [
       'static',
    ]
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_FILES_LOCATION)
    print("AWS S3 STATIC URL IS: ")
    print(AWS_S3_CUSTOM_DOMAIN)    
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # Where to store the static files (bucket folder name):
    # STATICFILES_LOCATION = 'static'
    # Storage type
    # STATICFILES_STORAGE = 'custom_storages.StaticStorage'

    # Where to store the media files (bucket folder name):
    # MEDIAFILES_LOCATION = 'media'
    # Storage type
    # DEFAULT_FIRE_STORAGE = 'custom_storages.MediaStorage'

    # STATIC_URL = 'https://{}/{}'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
'''