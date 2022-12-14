from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Check service variable will not work, Path is wrong
service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")

options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)  # handle value for parent window
handles = driver.window_handles  # return all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()  # close only parent window
