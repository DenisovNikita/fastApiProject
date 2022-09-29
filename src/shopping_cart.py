"""

Cart for shopping

"""
import pydantic

from contracts import Good


class Config:  # pylint: disable=too-few-public-methods
    """

    Config for shopping cart

    """

    arbitrary_types_allowed = True


@pydantic.dataclasses.dataclass(config=Config)
class ShoppingCart:
    """

    Shopping cart with goods from shop

    """

    def __init__(self):
        pass

    def add(self, good: Good):
        """

        Args:
            good: good which you want put in a cart

        Returns: is put successful

        """

    def remove(self, good: Good):
        """

        Args:
            good: good which you want remove from a cart

        Returns: is remove successfully

        """

    def release(self):
        """

        Returns: None

        """
