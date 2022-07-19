"""
Django settings for helloworld project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

from efficiency_platform_server.settings import CACHES
from .config import _CACHES

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nv8!ca8cq+oi*y5mi)%*#xxc)q%2wdt#i*lt(uftc8ycykew$c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 这里设置模板的路径为项目根目录(当然这个也可以设置)下的
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


# 日志文件目录
BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#         "default": {
#             "format": '%(asctime)s %(name)s  %(pathname)s:%(lineno)d %(module)s:%(funcName)s '
#                       '%(levelname)s- %(message)s',
#             "datefmt": "%Y-%m-%d %H:%M:%S"
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'default',
#             # 'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
#             'when': "D",
#             'interval': 1,
#             'formatter': 'default'
#         },
#         "request": {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/request.log'),
#             'formatter': 'default'
#         },
#         "server": {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/server.log'),
#             'formatter': 'default'
#         },
#         "root": {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/root.log'),
#             'formatter': 'default'
#         },

#         "db_backends": {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/db_backends.log'),
#             'formatter': 'default'
#         },
#         "autoreload": {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/autoreload.log'),
#             'formatter': 'default'
#         }
#     },
#     'loggers': {
#         # 应用中自定义日志记录器
#         'mylogger': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'file'],
#             'propagate': True,
#         },
#         "django": {
#             "level": "DEBUG",
#             "handlers": ["console", "file"],
#             'propagate': False,
#         },
#         "django.request": {
#             "level": "DEBUG",
#             "handlers": ["request"],
#             'propagate': False,
#         },
#         "django.server": {
#             "level": "DEBUG",
#             "handlers": ["server"],
#             'propagate': False,
#         },
#         "django.db.backends": {
#             "level": "DEBUG",
#             "handlers": ["db_backends"],
#             'propagate': False,
#         },
#         "django.utils.autoreload": {
#             "level": "INFO",
#             "handlers": ["autoreload"],
#             'propagate': False,
#         }
#     },
#     'root': {
#         "level": "DEBUG",
#         "handlers": ["root"],
#     }
# }

# Application definition

SECURE_SSL_REDIRECT = False
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # 安装session应用，默认创建项目自动添加
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sslserver',
    'ModelMusicians',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # 启用session中间件，默认创建项目自动添加
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2 # 指定sessionid在cookies中的保存时长 (两周)
SESSION_ENGINE = "django.contrib.sessions.backends.cache" # SESSION_ENGINE控制Django在何处存储会话数据，这里将Session的保存目的地更改为缓存
SESSION_CACHE_ALIAS = 'default' # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
SESSION_COOKIE_NAME = "session_id" # Session的cookie保存在浏览器上时的key

CACHES=_CACHES # CACHES用于设置缓存

ROOT_URLCONF = 'helloworld.urls'

WSGI_APPLICATION = 'helloworld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djmm',
        'HOST': '119.45.121.103',
        'PORT': 3306,
        'USER': 'cdb',
        'PASSWORD': '909089',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
