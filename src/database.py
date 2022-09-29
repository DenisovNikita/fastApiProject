"""

Service which connected to database

"""

from contracts import Good


class DataBase:
    """

    Mock DataBase which storage info about goods in the shop

    """

    def __init__(self):
        pass

    def find(self, good: Good):
        """

        Args:
            good: good which you want to find

        Returns: is there any matched goods

        """

    def add(self, good: Good):
        """

        Args:
            good: good which you want to add to database

        Returns: is adding successful

        """

    def show_goods(self):
        """

        Returns: available goods in the shop

        """

    def get_user_data(self, user_id: str):
        """

        Returns: user data

        """

    def decrease(self, good: Good):
        """

        Args:
            good: good which you want to remove from database

        Returns: is removing was successful

        """

    def increase(self, good: Good):
        """

        Args:
            good: good which you want to add to database

        Returns: is adding was successful

        """
