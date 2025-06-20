import os

class ReadFile:
    """
    Read file products.txt and return list of goods
    """
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__)) # Hold the folder of this module
        self.filepath = os.path.join(base_dir,"../data", "products.txt")
        self.list_of_products = []

        if os.path.isfile(self.filepath): # Check file is exist
            with open(self.filepath, "r", encoding="utf-8") as file:
                self.list_of_products = [line.strip() for line in file]

    @property
    def return_list_of_products(self):
        """
        Method that call as property and return value
        :return: list of products
        """
        return self.list_of_products