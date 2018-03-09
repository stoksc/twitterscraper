''' This module unit tests tools/db.
'''
import os
import time

import pytest

from tools.db import get_dynamodb_connection
from tools.db import get_dynamodb_table
from tools.db import create_table


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
    time.sleep(5) # wait until table create happens, boto3 is async'd to death
    table2.put_item(
        Item=ITEM
    )
    table2.scan()
    time.sleep(5) # and again
    table2.delete()
