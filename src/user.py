"""

User data

"""

from pydantic import BaseModel

from shopping_cart import ShoppingCart


class User(BaseModel):
    """

    User data

    """

    id: str
    shopping_cart: ShoppingCart
