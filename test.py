from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import xlrd
workbook = xlrd.open_workbook(r'C:\Users\U6033331\Desktop\Book1.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
cell_1 = worksheet.cell(0,0).value
cell_2 = worksheet.cell(0,1).value
keys = '"' + cell_1 + '"' + " " + 'AND' + " " + cell_2

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

driver.get("https://www.google.com")

m = driver.find_element(By.NAME,"q")
m.send_keys(keys)
m.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "IBM Watson").click()
# driver.get("https://www.google.com")
#
# driver.find_element(By.ID("lst-ib")).send_keys("Selenium")
#
# driver.find_element(By.ID("_fZl")).click()

#driver.find_element(By.LINK_TEXT("Google Search")).click()

#time.sleep(1)
#driver.close()