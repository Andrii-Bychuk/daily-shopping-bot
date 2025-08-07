import os
from modules.exceptions import ProductFileEmptyError, ProductFileMissingError

class ReadFile:
    """
    Reads 'products.txt' from '../data' folder and provides a list of products.
    If file is missing or empty, stores an error message.
    """
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__)) # Hold the folder of this module
        self.filepath = os.path.join(base_dir,"../data", "products.txt")

    @property
    def products(self) -> list:
        if not os.path.isfile(self.filepath): # Check file is exist
            raise ProductFileMissingError("The product file does not exist or have wrong name."
                                          "Create products.txt in 'data' folder.")

        with open(self.filepath, "r", encoding="utf-8") as file:
            list_of_products = [line.strip() for line in file]

        if not list_of_products:
            raise ProductFileEmptyError("The product file is empty. Add products, each on a new line.")

        return list_of_products
