import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('side', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_secret_sentence(browser, side):
    link = f"{side}"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR,"button.submit-submission").click()
    test_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert "Correct!" == test_text, test_text






