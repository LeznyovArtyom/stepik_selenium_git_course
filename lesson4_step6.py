from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)

    button = browser.find_element(By.ID, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()