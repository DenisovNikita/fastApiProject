# some_file.py
import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append('../src')

import pytest

# from shopping_cart import ShoppingCart

import pytest

# @pytest.fixture
# def shopping_cart_getter():
#     shopping_cart = ShoppingCart()
#     goods = []
#     [shopping_cart.add(good) for good in goods]
#     return shopping_cart
#
# def test_find(shopping_cart_getter):
#     print(*shopping_cart_getter)
#     assert False
