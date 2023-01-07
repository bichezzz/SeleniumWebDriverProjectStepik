import time
import math
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLessionParam:
    a = ""

    @pytest.mark.parametrize('url', ["236895",
                                     "236896",
                                     "236897",
                                     "236898",
                                     "236899",
                                     "236903",
                                     "236904",
                                     "236905"])
    def test_get_link(self, browser, url):
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)
        browser.implicitly_wait(1500)
        browser.find_element(By.CSS_SELECTOR, "#ember33").click()
        browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('psv.stas@yandex.ru')
        browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('Ioncheva433774')
        browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
        browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()
        time.sleep(30)
        info = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(By.CLASS_NAME, "smart-hints__hint").text
        )
        assert info == 'Correct!', f"{info}"

        if __name__ == "__main__":
            unittest.main()
