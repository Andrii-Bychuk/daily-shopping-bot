from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from modules.products import ReadFile
from config import SEARCH_PRODUCT_LIMIT


class MaudauParser:
    """
    Class for search given products
    """

    def __init__(self):
        self.start_url_search = "https://maudau.com.ua/search?text="
        self.all_response = []
        self.list_of_products = ReadFile().return_list_of_products
        self.list_of_search_urls = self.create_list_of_full_urls()
        self.result = []

        self.fetch_pages()
        self.parse_pages()


    def create_list_of_full_urls(self):
        """
        Create full URL paths with proper URL encoding.
        :return: list of search URLs
        """
        list_of_search_urls = []
        for url in self.list_of_products:
            list_of_search_urls.append(self.start_url_search + quote(url))

        return list_of_search_urls

    def fetch_pages(self):
        """
        Create a list of BeautifulSoup objects from existing URLs.
        :return: None
        """
        for url in self.list_of_search_urls:
            response = requests.get(url)
            page = response.text
            soup = BeautifulSoup(page, "html.parser")
            self.all_response.append(soup)


    def parse_pages(self):
        for response in self.all_response:
            five_products = response.find_all(class_="md-css-19huojj", limit=SEARCH_PRODUCT_LIMIT)
            for product in five_products:
                product_query = self.list_of_products[self.all_response.index(response)]
                product_name = product.find(class_="chakra-text md-css-bt097k").getText()
                product_image = product.find("img")["src"]
                product_price = product.find(class_="chakra-text md-css-1l6mpy8").getText()
                clean_price = product_price.replace("\xa0", " ")
                product_url = product.find("a")["href"]

                # Promo options
                try:
                    discount = product.find(class_="chakra-text md-css-bwyhlm").getText()
                    old_price = product.find(class_="chakra-text md-css-1o7tnuo").getText()
                except AttributeError:
                    discount = None
                    old_price = None

                self.result.append(
                    {
                        "product_query": product_query,
                        "product_name": product_name,
                        "image": product_image,
                        "price": clean_price,
                        "url": product_url,
                        "discount": discount if discount else "No Discount",
                        "old_price": old_price if old_price else "No Old price"
                    }
                )