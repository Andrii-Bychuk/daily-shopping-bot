from bs4 import BeautifulSoup
import requests
from modules.products import ReadFile


class MaudauParser:
    """
    Class for search given products
    """

    def __init__(self):
        self.start_url_search = "https://maudau.com.ua/search?text="
        self.response = ''
        self.list_of_products = ReadFile().return_list_of_products
        self.list_of_search_urls = []


    def create_list_of_full_urls(self):
        pass


    def search(self):
        self.response = requests.get(self.start_url_search)