from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
a = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")
    )
browser.find_element(By.CSS_SELECTOR, "#book").click()

b = browser.find_element(By.CSS_SELECTOR, "#input_value").text
c = str(math.log(abs(12*math.sin(int(b)))))
d = browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(c)
e = browser.find_element(By.CSS_SELECTOR, "#solve").click()


