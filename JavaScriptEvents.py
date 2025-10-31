import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver service
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)
time.sleep(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(15)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(5)
driver.get_screenshot_as_file(filename="img2.png")
driver.close()