import unittest

from src.url_parser import get_latest_publish_date
from src.url_parser import get_num_days_without_activity

#Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days.
class MyTestCase(unittest.TestCase):
    def setUp(self):
        url_1 = "http://joeroganexp.joerogan.libsynpro.com/rss"
        pass

    def test_get_latest_publish_date(self):
        url_1 = "http://joeroganexp.joerogan.libsynpro.com/rss"
        print(get_latest_publish_date(url_1))
        self.assertTrue(True)

    def test_get_num_days_without_activity(self):
        url_1 = "http://joeroganexp.joerogan.libsynpro.com/rss"
        latest_pub_date = get_latest_publish_date(url_1)
        get_num_days_without_activity(latest_pub_date)
        self.assertTrue(True)

if __name__ == '__main__':
    import url_parser
    unittest.main()
# feeds need to be taken in as a list , then parsed one by one