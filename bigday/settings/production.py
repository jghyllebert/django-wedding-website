import os

from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = [
    'kim-jonas2019.wedding'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
    }
}
