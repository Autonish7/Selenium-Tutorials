import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

filename = 'Company list.xlsx'
output_filename = 'Data_extracted_file.xlsx'

path = os.getcwd() + r'\Company list.xlsx'


cred = pandas.read_excel(path, sheet_name="Sheet2")
df = pandas.read_excel(path, sheet_name="Sheet1")

username = cred.iloc[0, 1]
password = cred.iloc[1, 1]

service = Service(os.getcwd() + r"\chromedriver.exe")
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.linkedin.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID, "session_key").send_keys(username)

driver.find_element(By.ID, "session_password").send_keys(password)

driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()
driver.implicitly_wait(10)

try:
    driver.find_element(By.CLASS_NAME, "secondary-action").click()

except NoSuchElementException:
    pass

time.sleep(2)

tot_employee = []
counter = 0

for company in df['List of companies']:

    driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input").send_keys(company)
    driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input").send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    elements = driver.find_elements(By.CLASS_NAME, "search-reusables__primary-filter")
    for element in elements:
        if element.text == "Companies":
            element.click()
            driver.implicitly_wait(5)
            time.sleep(2)
            break
        time.sleep(2)

    search_results = driver.find_elements(By.CLASS_NAME, "app-aware-link")

    for search_result in search_results:

        if company.lower() in search_result.text.lower() and search_result.tag_name == "a":
            driver.implicitly_wait(5)
            search_result.click()
            time.sleep(2)
            break

    try:
        emp_count = driver.find_element(By.PARTIAL_LINK_TEXT, "employees").text
        emp_count = emp_count.replace("employees", "")
        emp_count = emp_count.replace("See all", "")
        emp_count = emp_count.replace("on LinkedIn", "")
        emp_count = emp_count.strip()

    except NoSuchElementException:
        emp_count = "NA"

    df.loc[counter, 'Employee Count'] = emp_count
    counter = counter + 1

    time.sleep(2)
    driver.get("https://www.linkedin.com/feed/")

df.to_excel(os.getcwd() + "\\" + output_filename)

driver.close()
