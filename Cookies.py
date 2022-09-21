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

driver.get("https://www.amazon.in")
# Capture all cookies create by the browser
cookies = driver.get_cookies()

# Print the total number of cookies
print(len(cookies))

# Print all cookies. It is present in form of key-value pair
print(cookies)

# Add new cookies to the browser
cookie = {'name' : 'My_cookie', 'value':'1234567890'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()  # length of cookies is not constant
print(len(cookies))
print(cookies)

# delete the cookies, need to know the cookie
driver.delete_cookie("My_cookie")
cookies = driver.get_cookies()  # length of cookies is not constant
print(len(cookies))
print(cookies)

# delete all cookies from the browser
driver.delete_all_cookies()
cookies = driver.get_cookies()  # length of cookies is not constant
print(len(cookies))

driver.quit()