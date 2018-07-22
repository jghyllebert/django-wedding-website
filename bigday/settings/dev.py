import os

from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '82f862fd.ngrok.io',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
