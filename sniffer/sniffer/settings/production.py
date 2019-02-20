from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample', # 데이터베이스 이름
        'USER': 'root', # 접속 사용자 이름
        'PASSWORD': 'mysql', # 접속 비밀번호
        'HOST': 'localhost',
        'PORT': '3306', # 기본 포트
    }
}
# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1", # 1번 DB
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
