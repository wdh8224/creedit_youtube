from __future__ import absolute_import, unicode_literals

import os
from celery import Celery, signals


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
# CELERY_DEFAULT_QUEUE = 'ForCrawlingRegisterQueueAWSv3-edward'
CELERY_DEFAULT_QUEUE = 'ForCrawlingYoutubeChannel'
CELERY_TIMEZONE = 'Asia/Seoul'
CELERYD_MAX_TASKS_PER_CHILD = 128
CELERY_IGNORE_RESULT = True
CELERY_ENABLE_REMOTE_CONTROL = False
CELERYD_REDIRECT_STDOUTS_LEVEL = 'INFO'
CELERYD_HIJACK_ROOT_LOGGER = False

BROKER_URL = 'sqs://'
BROKER_TRANSPORT_OPTIONS = {'region': 'ap-northeast-1'}

app = Celery('Crawler_Youtube')

app.config_from_object("youtube_crawler.celery")
app.autodiscover_tasks(['youtube_crawler.worker'])

if __name__ == '__main__':
    app.start()
