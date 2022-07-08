from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[name=firstname]").send_keys("Dima")
    browser.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys("Bezsonov")
    browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("Bezsonov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "123.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()
#как приатаччить файл, вставить текст в вводное поле
