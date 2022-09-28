"""

Web application for honey selling

"""

from fastapi import FastAPI

from database import DataBase
from entities import Honey, Item

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


@app.post("/shop/")
async def shop(honey: Honey):
    """

    Args:
        honey: type of goods which you want to shop

    Returns: Is shopping was successful

    """
    if database.find(honey):
        database.sell(honey)
        return True
    return False
