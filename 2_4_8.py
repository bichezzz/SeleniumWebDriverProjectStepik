import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    btn = browser.find_element(By.CSS_SELECTOR, '#book')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
    solve = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", solve)
    x = browser.find_element(By.ID, 'input_value').text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    field = browser.find_element(By.ID, 'answer').send_keys(y)
    solve.click()

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()

