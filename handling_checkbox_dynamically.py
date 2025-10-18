import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "o    ption2":
        checkbox.click()
        break
time.sleep(5)
driver.close()