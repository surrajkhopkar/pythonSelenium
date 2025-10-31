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
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(30)
driver.switch_to.frame(frame_reference="mce_0_ifr")
time.sleep(5)
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
time.sleep(5)
