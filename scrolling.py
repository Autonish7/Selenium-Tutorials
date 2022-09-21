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

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# Scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,1000)", "")

# Scroll down the until it find the element
# flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll to the end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)
driver.close()