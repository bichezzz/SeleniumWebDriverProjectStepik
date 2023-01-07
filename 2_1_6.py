import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(service=Service('/Users/stanislavpolanicko/PycharmProjects/pythonProject1/chromedriver/chromedriver'))

try:
    browser.get(url)
    time.sleep(2)
    x_element = browser.find_element(By.ID, 'treasure')
    x_find = x_element.get_attribute('valuex')
    x = x_find
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > div > button').click()
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()