import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
time.sleep(5)
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")

# chaining operation
for product in products:
    product.find_element(By.XPATH,"div/button").click()
    time.sleep(5)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"promoBtn").click()
time.sleep(4)
driver.close()