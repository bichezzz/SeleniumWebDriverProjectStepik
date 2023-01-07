import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(url)
    time.sleep(10)
    enter = browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    login = browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('psv.stas@yandex.ru')
    password = browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('Ioncheva433774')
    submit = browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()