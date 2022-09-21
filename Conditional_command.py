from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

driver.get("""https://ipcpub.wipo.int/?notion=scheme&version=20220101&symbol="
           "none&menulang=en&lang=en&viewmode=f&fipcpc=no&showdeleted=yes"
           "&indexes=no&headings=yes&notes=yes&direction=o2n&initial=A&cwid"
           "=none&tree=no&searchmode=smart""")
driver.maximize_window()
print(driver.title)

textbox = driver.find_element(By.ID,"schemeSymbSearchForm")
Radio = driver.find_element(By.CSS_SELECTOR, "input[value=f]")

print(textbox.is_displayed())
print(textbox.is_enabled())
print(Radio.is_selected())

driver.quit()