"""

File with contracts

"""

from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    """

    Mock class to demonstrate FastAPI post request handling

    """

    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class Honey(BaseModel):
    """

    Type of honey which is available in the shop

    """

    quantity_kg: float
    type: str
