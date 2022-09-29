"""

Web application for honey selling

"""

from fastapi import FastAPI

from contracts import Good, Item
from database import DataBase
from shopping_cart import ShoppingCart
from user import User

app = FastAPI()


@app.get("/")
async def root():
    """

    Returns: json with message

    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """

    Args:
        name: your name

    Returns: message addressing to you

    """
    return {"message": f"Hello {name}"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/get_items/")
async def read_item(skip: int = 0, limit: int = 10):
    """

    Args:
        skip: number of items which will be skipped
        limit: limit on number of items in the response

    Returns: list of items

    """
    return fake_items_db[skip : skip + limit]


@app.post("/create_item/")
async def create_item(item: Item):
    """

    Args:
        item: item appropriate to contract

    Returns: your item

    """
    return item


database = DataBase()
shopping_cart = ShoppingCart()


@app.get("/show_goods/")
async def show_goods():
    """

    Returns: shop window of goods

    """
    return database.show_goods()


@app.post("/register_user/")
async def register_user(user: User):
    """

    Args:
        user: user data

    Returns: created user

    """
    return database.add(user)


@app.get("/get_user_data/{id}")
async def get_user_data(user_id: str):
    """

    Args:
        user_id: user id

    Returns: user data

    """
    return database.get_user_data(user_id)


@app.post("/add_to_cart/")
async def add_to_cart(good: Good):
    """

    Args:
        good: type of goods which you want to add

    Returns: Is adding was successful

    """
    if database.find(good):
        database.decrease(good)
        shopping_cart.add(good)
        return True
    return False


@app.post("/remove_from_cart/")
async def remove_from_cart(good: Good):
    """

    Args:
        good: type of goods which you want to remove

    Returns: Is removing was successful

    """

    shopping_cart.remove(good)
    database.increase(good)
    return True


@app.post("/release_cart")
async def release_cart():
    """

    Returns: None

    """
    shopping_cart.release()
