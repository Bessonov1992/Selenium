from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    c = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    d = str(math.log(abs(12*math.sin(int(c)))))
    e = browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(d)
    f = browser.find_element(By.CSS_SELECTOR, "button.btn").click()




    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()
# переход на новую вкладку

