from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from modules.products import ReadFile
from modules.rozetka_selenium import RozetkaSelenium
from config import SEARCH_PRODUCT_LIMIT


class AllParser:
    """
    Class for search given products
    """

    def __init__(self):
        self.start_url_search = ["https://maudau.com.ua/search?text=",
                                 "https://rozetka.com.ua/ua/search/?text="]
        self.all_response = {}
        self.list_of_products = ReadFile().return_list_of_products
        self.dict_of_search_urls = self.create_dict_of_full_urls()
        self.data_to_send = []

        self.fetch_pages()
        self.parse_pages()


    def create_dict_of_full_urls(self) -> dict:
        """
        Create full URL paths with proper URL encoding.
        :return: dict of search URLs
        """
        dict_of_search_urls = {}
        for search_url in self.start_url_search:
            inner_list= []

            for product in self.list_of_products:
                inner_list.append(search_url + quote(product))

            dict_of_search_urls[search_url] = inner_list

        return dict_of_search_urls


    def fetch_pages(self):
        """
        Create a list of BeautifulSoup objects from existing URLs.
        :return: None
        """
        for base_url_key, list_of_full_urls in self.dict_of_search_urls.items():
            inner_list = []

            for full_url in list_of_full_urls:
                if "maudau" in base_url_key:
                    response = requests.get(full_url)
                    page = response.text
                    soup = BeautifulSoup(page, "html.parser")
                    inner_list.append(soup)
                elif "rozetka" in base_url_key:
                    rozetka_object = RozetkaSelenium(full_url)
                    response = rozetka_object.result_html
                    soup = BeautifulSoup(response, "html.parser")
                    inner_list.append(soup)

            self.all_response[base_url_key] = inner_list


    def parse_pages(self):
        """
        Parse given pages and get needed data
        :return: list with inner dictionaries with all needed data
        """
        for base_url, response_list in self.all_response.items():
            # Maudau
            if "maudau" in base_url:
                for response in response_list:
                    received_products = response.find_all(class_="md-css-19huojj", limit=SEARCH_PRODUCT_LIMIT)
                    for product in received_products:
                        product_name = product.find(class_="chakra-text md-css-bt097k").getText()
                        product_image = product.find("img")["src"]
                        product_price = product.find(class_="chakra-text md-css-1l6mpy8").getText()
                        clean_price = product_price.replace("\xa0", " ")
                        product_url = product.find("a")["href"]

                        # Promo options
                        try:
                            discount = product.find(class_="chakra-text md-css-bwyhlm").getText()
                            old_price = product.find(class_="chakra-text md-css-1o7tnuo").getText()
                            clean_old_price = old_price.replace("\xa0", " ")

                        # If promo doesn't exist - assign None to variables
                        except AttributeError:
                            discount = None
                            clean_old_price = None

                        # Add data to list
                        self.data_to_send.append(
                            {
                                "website": "Maudau",
                                "product_name": product_name,
                                "image": product_image,
                                "price": clean_price,
                                "url": product_url,
                                "discount": discount if discount else "No Discount",
                                "old_price": clean_old_price if clean_old_price else "No Old price"
                            }
                        )
            # Rozetka
            elif "rozetka" in base_url:
                for response in response_list:
                    received_products = response.find_all(class_="catalog-grid__cell catalog-grid__cell_type_slim",
                                                          limit=SEARCH_PRODUCT_LIMIT)
                    for product in received_products:
                        product_name = product.find(class_="goods-tile__title").getText()
                        product_image = product.find("img")["src"]
                        product_price = product.find(class_="goods-tile__price-value").getText()
                        clean_price = product_price.replace("\xa0", " ")
                        product_url = product.find("a")["href"]

                        # Promo options
                        try:
                            discount = product.find(class_="goods-tile__label promo-label promo-label_"
                                                           "type_action").getText()
                            old_price = product.find(class_="goods-tile__price--old price--gray").getText()

                        # If promo doesn't exist - assign None to variables
                        except AttributeError:
                            discount = None
                            old_price = None

                        # Add data to list
                        self.data_to_send.append(
                            {
                                "website": "Rozetka",
                                "product_name": product_name,
                                "image": product_image,
                                "price": clean_price,
                                "url": product_url,
                                "discount": discount if discount else "No Discount",
                                "old_price": old_price if old_price else "No Old price"
                            }
                        )