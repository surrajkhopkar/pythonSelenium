import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# chrome driver service
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/dropdownsPractise//")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys('ind')
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(type(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(5)

# get dynamically updated text from the browser
assert driver.find_element(By.CSS_SELECTOR,"input[type='text']").get_attribute(name="value") == "Indiaaaa"
driver.close()