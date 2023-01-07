import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(service=Service('/Users/stanislavpolanicko/PycharmProjects/pythonProject1/chromedriver/chromedriver'))

try:
    browser.get(url)
    x_element = browser.find_element(By.ID, 'num1').text
    print(x_element)
    x = x_element
    y_element = browser.find_element(By.ID, 'num2').text
    print(y_element)
    y = y_element
    f = str(int(x) + int(y))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f)
    sub = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
    time.sleep(7)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()