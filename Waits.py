from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

# Selenium Python provides two types of waits - implicit & explicit.
# An explicit wait makes WebDriver wait for a specific condition to
# occur before proceeding further with execution.
# An implicit wait makes WebDriver poll the DOM for a certain amount
# of time when trying to locate an element.

# =====================Implicit Wait=================================
# Implicit wait applicable for all elements, completely based on time
# It affects the execution speed since each step waits for this wait till
# it gets the element it is looking for.

# driver.implicitly_wait(10)
# driver.get("https://demo.guru99.com/test/newtours/")
# assert "Welcome: Mercury Tours" in driver.title
# driver.maximize_window()
# driver.find_element(By.NAME,"userName").send_keys("mercury")
# driver.find_element(By.NAME,"password").send_keys("mercury")
# driver.find_element(By.NAME,"submit").click()
# driver.quit()

# =====================Explicit Wait=================================
# Explicit wait is based on condition, applicable for particular element
# It does not affect the execution speed since it is applicable to a particular
# element of the page.
# Conditions for explicit waits
# title_contains
# visibility_of_element_located
# presence_of_element_located
# title_is
# visibility_of
# element_selection_state_to_be
# presence_of_all_elements_located
# element_located_to_be_selected
# alert_is_present
# element_located_selection_state_to_b e
# staleness_of
# element_to_be_clickable
# invisibility_of_element_located
# frame_to_be_available_and_switch_to _it
# text_to_be_present_in_element_value
# text_to_be_present_in_element
# element_to_be_selected

driver.implicitly_wait(5)
driver.maximize_window()
# driver.get("https://www.expedia.com/")
driver.get("https://www.expedia.com/?pwaLob=wizard-flight-pwa")
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")  # origin
time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")  # destination

driver.find_element(By.ID, "flight-departing-hp-flight").clear()  # Need to clear previous values
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("16/10/2018")

driver.find_element(By.XPATH,"click on search button").click()
# Explicit Wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable(By.XPATH,"Capture availability of Radio button"))
element.click()
# In explicit wait, we need to define maximum time for which the application should wait.
time.sleep(5)
driver.quit()