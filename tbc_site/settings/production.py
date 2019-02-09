from __future__ import absolute_import, unicode_literals

from .base import *

# Parse database configuration from $DATABASE_URL
import os
import dj_database_url

env = os.environ.copy()
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Redirect all traffic to SSL via SecurityMiddleware
SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False

# POSTGRES_URL = 'HEROKU_POSTGRESQL_OLIVE_URL'
# DATABASES = {'default': dj_database_url.config(default=os.environ[POSTGRES_URL])}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# See https://chrxr.com/django-error-logging-configuration-heroku/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

try:
    pass
except ImportError:
    pass
