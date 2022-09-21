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

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")  # First frame
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(2)

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")  # Second Frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")  # Third Frame
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
time.sleep(5)

driver.quit()