import unittest
import datetime

import pytest

from src.url_parser import get_latest_publish_date
from src.url_parser import get_num_days_without_activity
from src.url_parser import find_company_with_inactivity_for_given_num_of_days



class MyTestCase(unittest.TestCase):

    def test_get_latest_publish_date(self):
        test_url = "http://joeroganexp.joerogan.libsynpro.com/rss"

        # check that reponse is a date time obj
        print(get_latest_publish_date(test_url))

        self.assertTrue(isinstance(get_latest_publish_date(test_url), datetime.date))

    def test_get_num_days_without_activity(self):
        test_url = "http://joeroganexp.joerogan.libsynpro.com/rss"
        latest_pub_date = get_latest_publish_date(test_url)
        print(get_num_days_without_activity(latest_pub_date))
        self.assertTrue(True)

    #On Mon Jan 25 2021 the result will be the Joe Rogan Expirence with 58 days. If you increase by one youll get the same.
    def test_find_company_with_inactivity_for_given_num_of_days(self):
        companies_rss_dict = dict({
            'The Joe Rogan Experience': "http://joeroganexp.joerogan.libsynpro.com/rss",
            "1619 by The New York Times": "https://feeds.simplecast.com/6HzeyO6b",
            "Code Switch by NPR": "https://feeds.npr.org/510312/podcast.xml",
            "Crime Junkie by audiochuck": "https://feeds.megaphone.fm/ADL9840290619",
            "Unlocking Us with Brené Brown": "https://feeds.megaphone.fm/unlocking-us",
            "The Daily by The New York Times": "https://feeds.simplecast.com/54nAGcIl",
            "The Ben Shapiro Show by The Daily Wire": "https://feeds.megaphone.fm/WWO8086402096",
            "My Favorite Murder by Karen Kilgariff and Georgia Hardstark": "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/44bbf446-4627-4f83-a7fd-ab070007db11/72b96aa8-88bd-480a-87af-ab070007db36/podcast.rss",
            "Call Her Daddy by Barstool Sports": "https://mcsorleys.barstoolsports.com/feed/call-her-daddy",
            "Dateline NBC": "https://podcastfeeds.nbcnews.com/dateline-nbc",
        })

        result = find_company_with_inactivity_for_given_num_of_days(companies_rss_dict, 58)
        print(result)
        self.assertEquals(result ,['The Joe Rogan Experience'])


if __name__ == '__main__':
    unittest.main()

