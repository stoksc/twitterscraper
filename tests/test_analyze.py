''' This module tests the analyze.py module of this program.
'''
import os

import pytest

from ..twitterscraper.tools.analyze import analyze_tweets
from ..twitterscraper.tools.analyze import analyze_tweets
from ..twitterscraper.tools.analyze import average_sentiment
from ..twitterscraper.tools.analyze import clean_text

from ..twitterscraper.tools.files import process_file


TEST_TWEETS = [
    {'text': '^^Hhhdas @a7sdASD&AS a'},
    {'text': '#hello #words'},
    {'text': '(ASDjlkdsad)&&& asd nm *DA(S)'},
    {'text': '0 000000000000000'},
    {'text': ''},
]
FILE_PATHS = [
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data1.json'),
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data2.json'),
]
KEYWORDS = [
    'python',
    'javascript'
]

def test_clean_text():
    texts = clean_text(TEST_TWEETS)


def test_sentiment_analysis():
    sentiment = average_sentiment(TEST_TWEETS)
    assert type(sentiment) is type(float())


def test_total_():
    for file_path in FILE_PATHS:
        for keyword in KEYWORDS:
            tweets = process_file(file_path)
            analyze_tweets(keyword, tweets)
