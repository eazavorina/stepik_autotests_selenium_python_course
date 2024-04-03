from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(y)

    browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)


finally:
    time.sleep(10)
    browser.quit