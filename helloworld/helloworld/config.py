# -*- coding: utf-8 -*-
# @time    : 2022/7/20 01:45 PM
# @Author  : chengdanbiao
# @file    : config.py


# 这个config.py文件并不是项目创建就有的，它完全是一个自定义的配置文件

# 配置生产/开发坏境  false 为开发坏境
IS_DEVELOPMENT = False


# 开发坏境
CACHES_DEV = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache', # django-redis是可以让django使用redis作为缓存存储的第三方库。其实除了Redis,缓存其实还可以写在文件、数据库、内存中
        'LOCATION': 'redis://192.168.7.204:6379/1',
        'TIMEOUT': 300, # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
        'KEY_PREFIX': 'cdb', # 缓存键的前缀
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 生产坏境
CACHES_PRO = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 把这里缓存你的redis服务器ip和port
        "LOCATION": "redis://192.168.2.205:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

_CACHES = CACHES_PRO if IS_DEVELOPMENT else CACHES_PRO