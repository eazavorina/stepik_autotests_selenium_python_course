from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, 'trollface').click()

    original_tab = browser.current_window_handle
    new_tab = browser.window_handles[1]

    browser.switch_to.window(new_tab)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(y)

    browser.find_element(By.CLASS_NAME, 'btn').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)


finally:
    time.sleep(10)
    browser.quit