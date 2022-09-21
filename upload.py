from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
filename = r"C:\Users\U6033331\Documents\Misc Projects\Badminton Expenses.xlsx"
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)
driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys(filename)
driver.quit()