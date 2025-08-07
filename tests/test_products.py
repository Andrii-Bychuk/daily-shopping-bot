import os
import pytest
from modules.products import ReadFile
from modules.exceptions import ProductFileEmptyError, ProductFileMissingError

TEST_FILE = "tests/test_products.txt"

class TestReadFile:
    def setup_method(self):
        self.reader = ReadFile()
        self.reader.filepath = TEST_FILE # New test file path

    def teardown_method(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_valid_product_file(self):
        with open(TEST_FILE, "w", encoding="utf-8") as file:
            file.write("cofee\ntea\n")

        products = self.reader.products
        assert products == ["cofee", "tea"]

    def test_missing_file_raises_error(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        with pytest.raises(ProductFileMissingError):
            _ = self.reader.products

    def test_empty_file_raises_error(self):
        with open(TEST_FILE, "w", encoding="utf-8") as f:
            f.write("")

        with pytest.raises(ProductFileEmptyError):
            _ = self.reader.products