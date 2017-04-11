"""
Django settings for TestProject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
#
import os

from .base import *
#
#
# # DEBUG = True
# ALLOWED_HOSTS = ['10.55.55.55', '192.168.33.15', '192.168.0.92']
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('DATABASE_NAME', 'postgres'),
#         'USER': os.getenv('DATABASE_USER', 'postgres'),
#         'PASSWORD': os.getenv('DATABASE_PASSWORD', 'password'),
#         'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
#         'PORT': os.getenv('DATABASE_PORT', '5432'),
#     }
# }
#
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #          'NAME': 'apmitalia_db',
# #          'USER': 'apmitalia',
# #          'PASSWORD': 'Jes17us.20',
# #          'HOST': '127.0.0.1',
# #          'PORT': '5432',
# #     }
# # }

