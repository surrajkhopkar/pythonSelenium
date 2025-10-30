import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome driver service
name = "Joe"
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.find_element(By.NAME,"enter-name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(5)

# switch from browser to alert mode
alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)


driver.close()