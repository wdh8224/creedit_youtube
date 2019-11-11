import os
import unittest

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
unittest.TestCase.maxDiff = None

USE_TZ = True
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        "CONN_MAX_AGE": 1800,
        'HOST': 'creedit.cguzjiix71m6.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'USER': 'ehdguse',
        'PASSWORD': 'ehdgus93',
        'NAME': 'creedit',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET time_zone = \'+09:00\';"
        },
        'TIME_ZONE': 'Asia/Seoul'
    }
}
DEFAULT_REQUEST_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                             "Chrome/46.0.2490.80 Safari/537.36"
DEFAULT_REQUEST_ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
DEFAULT_REQUEST_HEADERS = {
    "Accept": DEFAULT_REQUEST_ACCEPT,
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4",
    "User-Agent": DEFAULT_REQUEST_USER_AGENT
}

SECRET_KEY = '...'
INSTALLED_APPS = ['youtube_crawler']
WSGI_APPLICATION = get_wsgi_application()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGER_OPTION = os.getenv("LOGGER_OPTION", 'json_logging')
