import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(5)
driver.find_element(By.NAME,"name").send_keys("John")
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("password")
driver.find_element(By.CLASS_NAME,"form-check").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(10)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)
message = driver.find_element(By.CLASS_NAME,"alert").text
assert "Success" in message
print(message)
driver.close()
