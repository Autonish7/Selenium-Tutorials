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

driver.get("https://cosmocode.io/automation-practice-webtable/")

rows = len(driver.find_elements(By.XPATH, "//*[@id='countries']/tbody/tr"))  # count number of rows
columns = len(driver.find_elements(By.XPATH, "//*[@id='countries']/tbody/tr[1]/td"))  # count number of columns

for row in range(2, rows+1):
    for column in range(2, columns+1):
        value = driver.find_element(By.XPATH, "//*[@id='countries']/tbody/tr[{}]/td[{}]".format(str(row),str(column))).text
        print(value, end='   ')
    print()

time.sleep(5)
driver.close()