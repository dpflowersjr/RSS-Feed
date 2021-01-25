import urllib3
import xmltodict
import traceback
import feedparser
from datetime import datetime, timedelta

def get_latest_publish_date(url):

    news_Feed = feedparser.parse(url)
    entry = news_Feed.entries[0]
    latest_publish_date = datetime.strptime(str(entry.get('published')), "%a, %d %b %Y %H:%M:%S %z")

    return latest_publish_date


def get_num_days_without_activity(date):
    current_date = datetime.today()
    count = current_date - date
    return count.days

