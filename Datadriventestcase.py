import ExcelUtil
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

driver.get(r"https://demo.guru99.com/test/newtours/")
path = r"C:\Users\U6033331\Desktop\Book1.xlsx"
rows = ExcelUtil.getRowCount(path, 'Sheet1')
for row in range(2, rows+1):
    username = ExcelUtil.readData(path,'Sheet1',row,1 )
    password = ExcelUtil.readData(path, 'Sheet1',row,2)

    driver.find_element(By.NAME, "userName").send_keys((username))
    driver.find_element(By.NAME, "password").send_keys((password))
    driver.find_element(By.NAME, "submit").click()

    if driver.title == "Login: Mercury Tours":
        print("test case is pass")
        ExcelUtil.writeData(path, 'Sheet1', row, 3, "test passed")
    else:
        ExcelUtil.writeData(path, 'Sheet1', row, 3, "Not passed")

    driver.get(r"https://demo.guru99.com/test/newtours/")

