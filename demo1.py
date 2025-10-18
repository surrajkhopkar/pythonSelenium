import time
from selenium import webdriver

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("http://google.com")