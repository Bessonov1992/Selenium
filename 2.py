from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, "#num1").text
    b = browser.find_element(By.CSS_SELECTOR, "#num2").text
    c = str(int(a)+int(b))
    print(c)
    d = Select(browser.find_element(By.TAG_NAME ,"select"))
    d.select_by_visible_text(c)
    
    # Ваш код, который заполняет обязательные поля
    # Отправляем заполненную форму
    f = browser.find_element(By.CSS_SELECTOR, "button.btn")
    f.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


