import math
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome(service=Service('/Users/stanislavpolanicko/PycharmProjects/pythonProject1/chromedriver/chromedriver'))

try:
    browser.get(url)
    button = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    button = browser.find_element(By.ID, "answer")
    field = browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()