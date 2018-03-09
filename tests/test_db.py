''' This module unit tests tools/db.
'''
import os
import time

import pytest

from ..twitterscraper.tools.db import get_dynamodb_connection
from ..twitterscraper.tools.db import get_dynamodb_table
from ..twitterscraper.tools.db import create_table


AWS_AK, AWS_SK = os.environ['AWS_AK'], os.environ['AWS_SK']
TEST_TABLE = 'test_table'
ITEM = {
    'framework': 'something',
    'unix_time': 1213,
    'otherstuff': 400,
}


def test_table():
    table1 = get_dynamodb_table(
        access_key=AWS_AK,
        secret_key=AWS_SK,
        table=TEST_TABLE
    )
    table2 = get_dynamodb_table(
        access_key=AWS_AK,
        secret_key=AWS_SK,
        table=TEST_TABLE
    )
    assert table1 == table2
