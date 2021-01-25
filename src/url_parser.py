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
    if 'GMT' in entry.get('published'):
        timezone_adjustment = str(entry.get('published')).replace('GMT', "+0000")
        return datetime.strptime(timezone_adjustment,"%a, %d %b %Y %H:%M:%S %z")

    latest_publish_date = datetime.strptime(str(entry.get('published')), "%a, %d %b %Y %H:%M:%S %z")

    return latest_publish_date


def get_num_days_without_activity(date):
    # subtract the number of dates via milisecods to get result of days away from current
    current_date = datetime.now().replace(tzinfo=utc)
    count = current_date - date.replace(tzinfo=utc)
    return count.days

def find_company_with_inactivity_for_given_num_of_days( dict , num_inactive_days):

    #loop through dict and check days of inactivity
    companies = []

    try:
        for company in dict:
            latest_date = get_latest_publish_date(dict.get(company))
            inactive_day_count = get_num_days_without_activity(latest_date)
            if inactive_day_count == num_inactive_days:
                companies.append(company)

        return companies
    except:
        traceback.print_exc()
    return companies