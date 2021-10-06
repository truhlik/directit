from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'directit',
        'USER': 'directit',
        'PASSWORD': 'directit',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
SECRET_KEY = 'testing'
CELERY_BROKER_URL = 'redis://redis/0'
CELERY_RESULT_BACKEND = 'redis://redis/0'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
