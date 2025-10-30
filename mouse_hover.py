import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# chrome driver service
name = "Joe"
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(5)
driver.close()