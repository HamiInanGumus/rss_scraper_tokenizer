# This module helps rss_scraper_tokenized_entries, rss_scraper_freq_dist.py
# and rss_scraper_collocations via providing methods to scrape the feed and
# instantiate a tokenized text

import nltk, re, pprint
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib import request
import feedparser
from urllib.request import Request, urlopen

class RssTokenizedText:
    """A class for modelling tokenized text from rss/ atom feeds """
    def rss_address():
        address = input("Please provide rss/atom feed url: ")
        llog = feedparser.parse(address)
        return llog

    def tokenize():
        rss_tokenized_entries = []
        log = RssTokenizedText.rss_address()
        for x in range(len(log.entries)):
            post = log.entries[x]
            url = post.links[0]['href']
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko)\
              Chrome/86.0.4240.75 Safari/537.36'}
            req = Request(url, headers=headers)
            webpage = urlopen(req).read()
            raw = BeautifulSoup(webpage, 'html.parser',\
             from_encoding="iso-8859-1").get_text()
            rss_tokens = word_tokenize(raw)
            rss_tokenized_entries.append(rss_tokens)
            rss_tokenized_entries=rss_tokenized_entries[:]
        return rss_tokenized_entries