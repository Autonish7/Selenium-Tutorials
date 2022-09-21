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

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# to find number of input boxes in a web page
input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')  # this will capture multiple elements
print(input_boxes)
print(len(input_boxes))

status = driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Displayed or not:", status)

status = driver.find_element(By.ID,'RESULT_TextField-2').is_enabled()
print("Enabled or not:", status)

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Nishant")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Chauhan")
driver.find_element(By.ID,'RESULT_TextField-3').send_keys("9998886665")
driver.find_element(By.ID,'RESULT_TextField-4').send_keys("India")
driver.find_element(By.ID,'RESULT_TextField-5').send_keys("Mumbai")
driver.find_element(By.ID,'RESULT_TextField-6').send_keys("Mumbai.India@gmail.com")

# Radiobutton - Selected or Not
driver.find_element(By.ID,'RESULT_RadioButton-7_1').is_selected()
driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label").click()

# CheckButton
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[7]/td/label").click()

# dropdown
drop = Select(driver.find_element(By.ID,"RESULT_RadioButton-9"))  # select class object
# drop.select_by_visible_text("Morning")  # Select based on values
drop.select_by_index(2)  # Afternoon
# drop.select_by_value("Radio-2")  # Based on item
# count and Capture all the options and print them as output
print(len(drop.options))
for option in drop.options:
    print(option.text)
time.sleep(5)
driver.quit()