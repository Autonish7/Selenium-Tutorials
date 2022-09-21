from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

service = Service(r"C:\Users\nishant.chauhan\OneDrive - Everest Group\Documents\Python Material\Drivers\Selenium Basic\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

# ======  Mouse Hover Action - check code, not working  ======== #
# driver.get("https://opensource-demp.orangehrmlive.com")
# driver.find_element(By.ID,"txtUsername").clear()
# driver.find_element(By.ID,"txtPassword").clear()
# driver.find_element(By.ID,"txtUsername").send_keys("admin")
# driver.find_element(By.ID,"txtPassword").send_keys("admin123")
# driver.find_element(By.ID,"loginAsButtonGroup").click()
# admin = driver.find_element(By.XPATH, 'admin Xpath')
# user_management = driver.find_element(By.XPATH, 'user_management Xpath')
# user = driver.find_element(By.XPATH, 'user')
# actions = ActionChains(driver)
# actions.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()

# ========= double click() ========== #
# driver.get("https://testautomationpractice.blogspot.com/")
# element = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
# actions = ActionChains(driver)
# actions.double_click(element).click().perform()

# ========= double click() ========== #
# driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
# button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")
# actions = ActionChains(driver)
# actions.context_click(button).perform()

# ========== Drag and Drop ========== #
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source = driver.find_element(By.XPATH, "//*[@id='box6']")
target = driver.find_element(By.XPATH, "//*[@id='box106']")
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
time.sleep(5)
driver.close()

