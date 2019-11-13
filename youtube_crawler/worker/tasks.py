import json
import re

from datetime import datetime
import pytz
import requests
from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger

from youtube_crawler.celery import app

logger = get_task_logger(__name__)

API_PATH = 'http://openapi.airkorea.or.kr/openapi/services/rest'
WEATHER_API_PATH = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2'


@app.task(bind=True, name="youtube_crawler.crawl_youtube_channel", soft_time_limit=300, time_limit=360,
          ignore_result=True)
def crawl_youtube_channel(self, **kwargs):
    """
       유튜브 채널정보크롤링
    :param self:
    :param kwargs:
    :return:
    """
    sample_url = "https://www.youtube.com/channel/UCbFzvzDu17eDZ3RIeaLRswQ"
    if "/user/" in sample_url:
        type = "userId"
        type_id = re.search("user\/(.+)\/", sample_url).group(1)
    else:
        type = "channelId"
        type_id = re.search("channel\/(.+)", sample_url).group(1)

    url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyBfpji4AkOB6ddNAYs9PXBlPPHHFt-YZOQ" \
          "&{}={}&part=snippet,id&order=date&maxResults=20".format(type, type_id)
    response = requests.get(url)
    # json.loads(requests.get(
        # "https://www.googleapis.com/youtube/v3/search?key=AIzaSyBfpji4AkOB6ddNAYs9PXBlPPHHFt-YZOQ&part=snippet&type=video&videoCategoryId=10").content)
    items = json.loads(response.content)['items']
    results = [parse_items(item) for item in items]
    return True


def parse_items(item):
    title = item["snippet"]["title"]
    published_at = pytz.timezone('Asia/Taipei').localize(
        datetime.strptime(item["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%S.%fZ"))
    author = item['snippet']['channelTitle']
    video_id = item['id']['videoId']
    article_url = get_article_url(video_id)
    description = item['snippet']['description']
    infos = get_statics_info(video_id)
    category_infos = get_all_category_info()
    return article_url, title, author, published_at, description, infos


def get_article_url(video_id):
    article_url = "https://www.youtube.com/embed/{}".format(video_id)
    return article_url


def get_statics_info(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics&id={}&key=AIzaSyBfpji4AkOB6ddNAYs9PXBlPPHHFt-YZOQ".format(video_id)
    response = requests.get(url)
    infos = json.loads(response.content)['items'][0]['statistics']
    return infos


def get_all_category_info():
    url = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=KR&key=AIzaSyBfpji4AkOB6ddNAYs9PXBlPPHHFt-YZOQ"
    response = requests.get(url)
    infos = json.loads(response.content)['items']
    return infos