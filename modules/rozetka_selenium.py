from selenium import webdriver
import time


class RozetkaSelenium:
    """
    Processes JS from website by Selenium and save pure html in object.
    """

    def __init__(self, query: str):
        # Keep Chrome browser open after program finishes
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                    "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

        # Create and configure the Chrome webdriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.query = query
        self.result_html = ''

        self.load_result_page()
        self.close()


    def load_result_page(self):
        self.driver.get(self.query)
        time.sleep(5)
        self.result_html = self.driver.page_source


    def close(self):
        self.driver.quit()
