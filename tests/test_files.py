''' This module unit tests tools/files.
'''
import os

import pytest

from tools.files import process_file


FILE_PATHS = [
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data1.json'),
    os.path.join(os.getcwd(), 'tests', 'test_data', 'test_data2.json'),
]


def test_file_operations():
    ''' Tests files operations function correctly.
    '''
    for file_path in FILE_PATHS:
        tweets = process_file(file_path)
        assert type(tweets) is type(list())
