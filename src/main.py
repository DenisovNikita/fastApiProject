# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import FastAPI

from database import DataBase
from entities import Honey, Item

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/get_items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.post("/create_item/")
async def create_item(item: Item):
    return item


database = DataBase()

@app.post("/shop/")
async def shop(honey: Honey):
    if database.find(honey):
        database.sell(honey)
        return True
    return False
