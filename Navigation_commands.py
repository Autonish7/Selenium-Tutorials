from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Magnetic_resonance_imaging")
print(driver.title)
driver.get("https://en.wikipedia.org/wiki/Ultrasound")
print(driver.title)

driver.back()
print("First page : ",driver.title)
print("First URL : ",driver.current_url)

driver.forward()
print("Second page : ",driver.title)
print("Second URL : ",driver.current_url)

#time.sleep(5)
# driver.close() currently focused browser
driver.quit()