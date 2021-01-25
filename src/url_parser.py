import urllib3
import xmltodict
import traceback


def get_xml(url):

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data

# last build/ publish date
def get_latest_publish_date(data):
    count = 0
    return count