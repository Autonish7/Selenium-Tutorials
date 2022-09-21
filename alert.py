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

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()

# driver.switch_to.alert.accept()  # to accept the alert
driver.switch_to.alert.dismiss()
time.sleep(5)

driver.quit()