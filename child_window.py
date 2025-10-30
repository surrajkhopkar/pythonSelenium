import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver service
name = "Joe"
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://the-internet.herokuapp.com/windows")
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME,"h3")))
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(10)
windows_opened = driver.window_handles
print(windows_opened)
driver.switch_to.window(window_name=windows_opened[1])
time.sleep(3)
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(window_name=windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
