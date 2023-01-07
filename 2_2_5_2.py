import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome(service=Service('/Users/stanislavpolanicko/PycharmProjects/pythonProject1/chromedriver/chromedriver'))

try:
    browser.get(url)
    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    button = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    field = browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
except Exception as ex:
    print(ex)
finally:
    time.sleep(10)
    browser.close()
    browser.quit()