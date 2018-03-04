''' This module tests the analyze.py module of this program.
'''

import pytest

from tools.analyze import average_sentiment
from tools.analyze import clean_text


TEST_TWEETS = [
    {'text': '^^Hhhdas @a7sdASD&AS a'},
    {'text': '#hello #words'},
    {'text': '(ASDjlkdsad)&&& asd nm *DA(S)'},
    {'text': '0 000000000000000'},
    {'text': ''},
]

def test_clean_text():
    ''' This function tests the text cleaning regexs in the analyze module.
    '''
    texts = clean_text(TEST_TWEETS)


def test_sentiment_analysis():
    ''' This function tests the sentiment analysis functionality.
    '''
    sentiment = average_sentiment(TEST_TWEETS)
    assert type(sentiment) is type(float())
