import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(executable_path='/Users/surajkhopkar/Library/CloudStorage/GoogleDrive-surraj@surrajkhopkar.com/My Drive/Career/'
                        'CodeBase/PythonSelenium/drivers/chromedriver')

driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com")
time.sleep(5)
driver.maximize_window()
driver.title()