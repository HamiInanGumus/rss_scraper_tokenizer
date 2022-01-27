# This program tokenizes entries/articles from rss/atom feed by scraping the
# feed after the url for the feed is provided by the user. It uses
# rss_scraper_tokenizedtext_class and its method to scrape the feed and
# instantiate tokenized text

import nltk, re, pprint
from rss_scraper_tokenizedtext_class import *

rss_tokenized_entries = RssTokenizedText.tokenize()
print("Name of the tokenized entries list: 'rss_tokenized_entries' | \
use len(rss_tokenized_entries) to find the number of rss feed entries | \
use rss_tokenized_entries[] or print(rss_tokenized_entries[]) with an index \
number to see the content.")
