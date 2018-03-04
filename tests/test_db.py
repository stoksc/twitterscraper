''' This module unit tests tools/db.
'''
import time

import pytest

from tools.keys import AWS_AK, AWS_SK
from tools.db import get_dynamodb_connection
from tools.db import get_dynamodb_table
from tools.db import create_table


TEST_TABLE = 'test_table'

ITEM = {
    'entry_id': 0,
    'otherstuff': 400,
}

def test_table():
    ''' Tests tables can be created.
    '''
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
    time.sleep(10) # wait until table create happens
    table2.put_item(
        Item=ITEM
    )
    table2.scan()
    table2.delete()
