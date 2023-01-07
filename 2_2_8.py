import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(service=Service('/Users/stanislavpolanicko/PycharmProjects/pythonProject1/chromedriver/chromedriver'))

try:
    browser.get(url)
    first_name = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)').send_keys('Stanislav')
    last_name = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)').send_keys('Polianichko')
    email = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)').send_keys('test@test.com')
    time.sleep(1)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = '2_amazon.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, '//*[@id="file"]').send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()