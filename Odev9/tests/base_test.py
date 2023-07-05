import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = "https://seleniumautomation.inone.useinsider.com/"

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
