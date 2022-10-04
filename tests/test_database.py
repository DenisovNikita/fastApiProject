# some_file.py
import sys

# from contracts import Good

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../src')

import pytest

# from database import DataBase

# @pytest.fixture
# def database_getter():
#     database = DataBase()
#     goods = []
#     [database.add(good) for good in goods]
#     return database
#
# def test_find(database_getter):
#     print(*database_getter)
#     assert False
#
# def test_add(database_getter):
#     good = Good()
#     database = database_getter
#     database.add(good)
#     assert database.find(good)