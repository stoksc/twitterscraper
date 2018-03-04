''' This module tests the retrieval module of this program.
'''
import json
import os

import pytest

from tools.retrieval import clean_tweet
from tools.retrieval import start_stream
from tools.retrieval import IntervalListener

TEST_HASHTAG = 'test'

FILE_PATH = os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data1.json')


def test_clean_tweet():
    with open(FILE_PATH, 'r') as f:
        for entry in f:
            clean_tweet(json.loads(entry))


def test_start_stream():
    stream = start_stream(hashtag=TEST_HASHTAG)
    stream.disconnect()


def test_interval_listener():
    assert IntervalListener()
