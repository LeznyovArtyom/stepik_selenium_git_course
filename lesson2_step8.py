from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    for element in browser.find_elements(By.CSS_SELECTOR, "[type='text']"):
       element.send_keys("текст")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    file_input = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file_input.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()