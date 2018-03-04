''' This module unit tests tools/files.
'''
import os

import pytest

from tools.files import process_file


FILE_PATH = os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data1.json')

def test_file_operations():
    ''' Tests files operations function correctly.
    '''
    tweets = process_file(FILE_PATH)
    assert type(tweets) is type(list())
