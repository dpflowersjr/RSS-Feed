import unittest

from src.url_parser import get_xml

#Given a Dictionary keyed by Company and valued by RSS feed url, write a function that determines which companies had no activity for a given number of days.
class MyTestCase(unittest.TestCase):
    def setUp(self):
        url_1 = "http://joeroganexp.joerogan.libsynpro.com/rss"
        pass

    def test_get_xml(self):
        url_1 = "http://joeroganexp.joerogan.libsynpro.com/rss"
        print(get_xml(url_1))
        self.assertTrue(True)


if __name__ == '__main__':
    import url_parser
    unittest.main()
# feeds need to be taken in as a list , then parsed one by one