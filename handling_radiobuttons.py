import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        break

time.sleep(10)
driver.close()

