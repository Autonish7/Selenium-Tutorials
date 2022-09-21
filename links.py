from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/")
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))  # print number of link present in a page

# for link in links:
#     print(link.text)
# driver.find_element(By.LINK_TEXT, "REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()  # Case sensitive
time.sleep(5)
driver.quit()