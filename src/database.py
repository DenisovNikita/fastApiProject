"""

Service which connected to database

"""

from entities import Honey


class DataBase:
    """

    Mock DataBase which storage info about goods in the shop

    """

    def __init__(self):
        pass

    def find(self, honey: Honey):
        """

        Args:
            honey: type of goods which you want to find

        Returns: is there any matched goods

        """

    def sell(self, honey: Honey):
        """

        Args:
            honey: type of goods which you want to sell

        Returns: is selling successful

        """
