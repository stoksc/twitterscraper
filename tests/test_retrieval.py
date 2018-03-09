''' This module tests the retrieval module of this program.
'''
import json
import os

import pytest

from tools.retrieval import clean_tweet
from tools.retrieval import start_stream
from tools.retrieval import IntervalListener


TEST_HASHTAGS = [
    'julia',
    'pascal',
]
FILE_PATHS = [
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data1.json'),
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data2.json'),
]


def test_clean_tweet():
    for file_path in FILE_PATHS:
        with open(file_path, 'r') as f:
            for entry in f:
                clean_tweet(json.loads(entry))


def test_start_stream():
    stream = start_stream(hashtags=TEST_HASHTAGS)
    stream.disconnect()


def test_interval_listener():
    assert IntervalListener()
