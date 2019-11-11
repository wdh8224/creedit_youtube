from celery.utils.log import get_task_logger
from django.db import models
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

__all__ = ['YoutubeData']

logger = get_task_logger(__name__)


class YoutubeData(models.Model):
    id = models.AutoField(primary_key=True)
    channel_name = models.CharField(max_length=255)
    updated_at = models.IntegerField()

    class Meta:
        db_table = 'youtube_data'



