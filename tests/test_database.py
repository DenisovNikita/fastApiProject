# some_file.py
import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../src')

import pytest

from database import DataBase

import pytest

@pytest.fixture
def database_getter():
    database = DataBase()
    goods = []
    [database.add(good) for good in goods]
    return database

def test_find(database_getter):
    print(*database_getter)
    assert False
