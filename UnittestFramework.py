import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# class Test(unittest.TestCase):
#     def test_firstTest(self):
#         print("This is my first unit test case")

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()


class SearchEngineTest(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://www.google.com/")
        print("Title of the page is : ", self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://bing.com/")
        print("Title of the page is : ", self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()