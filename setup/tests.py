from os import curdir, path, sep
from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        driver = "chromedriver.exe"
        self.browser = webdriver.Chrome(f"{path.abspath(curdir)}{sep}{driver}")

    def tearDown(self) -> None:
        self.browser.quit()
