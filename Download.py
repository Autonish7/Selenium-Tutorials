from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options

# ===========Firefox setting ======================#
fp = webdriver.FirefoxProfile
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf")  #Mime type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", r"C:\Users\U6033331\Desktop")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)
# ================ends==============================#

# edgeoptions = Options()
# edgeoptions.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\U6033331\Desktop"})

service = Service(r"C:\Users\U6033331\Anaconda3\Drivers\edgedriver_win32\msedgedriver.exe")
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

# download text files
driver.find_element(By.ID,"textbox").send_keys("testing download text file")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()
time.sleep(5)

# download PDF files
driver.find_element(By.ID, "pdfbox").send_keys("Generate PDF files")
driver.find_element(By.ID, "createPdf").click()
driver.find_element(By.ID, "pdf-link-to-download").click()
time.sleep(5)
driver.quit()