from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from modules.products import ReadFile


class MaudauParser:
    """
    Class for search given products
    """

    def __init__(self):
        self.start_url_search = "https://maudau.com.ua/search?text="
        self.response = ''
        self.list_of_products = ReadFile().return_list_of_products
        self.list_of_search_urls = self.create_list_of_full_urls()


    def create_list_of_full_urls(self):
        """
        Create full url path with correct URL-encoding
        :return: list of search urls
        """
        list_of_search_urls = []
        for url in self.list_of_products:
            list_of_search_urls.append(self.start_url_search + quote(url))

        return list_of_search_urls

    def search(self):
        self.response = requests.get(self.start_url_search)
