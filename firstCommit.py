from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://games-sb.hhs-test.net/"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "#login").send_keys("swollow")
    browser.find_element(By.CSS_SELECTOR, "#password").send_keys("2997")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div:nth-child(1) > button").click()
    browser.find_element(By.CSS_SELECTOR, "ul.dropdown-menu > :nth-child(2)").click()
    browser.find_element(By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div:nth-child(2) > button").click()
    browser.find_element(By.CSS_SELECTOR, "#lang > li:nth-child(5) > a").click()
    browser.find_element(By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div:nth-child(3) > button").click()
    browser.find_element(By.CSS_SELECTOR, "#cur > li:nth-child(7) > a").click()
    browser.find_element(By.CSS_SELECTOR, "#balance[class='form-control']").send_keys("99")
    browser.find_element(By.CSS_SELECTOR, "body > div.container > div:nth-child(1) > div:nth-child(4) > div > div > button").click()
    browser.find_element(By.CSS_SELECTOR, "div.fullstate-html5-evoplay-slots-wrap > ul >li:nth-child(3) > a:nth-child(1)").click()
    time.sleep(1)
finally:
    time.sleep(10)
    browser.quit()
    