from time import timezone

import urllib3
import xmltodict
import traceback
import feedparser
from datetime import datetime, timedelta

from pytz import utc


def get_latest_publish_date(url):

    news_Feed = feedparser.parse(url)
    entry = news_Feed.entries[0]
    latest_publish_date = datetime.strptime(str(entry.get('published')), "%a, %d %b %Y %H:%M:%S %z")

    return latest_publish_date


def get_num_days_without_activity(date):
    current_date = datetime.now().replace(tzinfo=utc)
    count = current_date - date.replace(tzinfo=utc)
    return count.days

