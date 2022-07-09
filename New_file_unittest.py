from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class unit(unittest.TestCase):
    def test_unit_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys("Yarovoy")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys("Yarovoy@mail.ru")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Done")


        time.sleep(10)
        browser.quit()

    def test_unit_2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys("Yarovoy")
        browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys("Yarovoy@mail.ru")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Done")

        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
