from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Анна')
    browser.find_element(By.NAME, 'lastname').send_keys('Автоматова')
    browser.find_element(By.NAME, 'email').send_keys('fakemail@fake.com')

    current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8_upload_file.py'))
    file_path = os.path.join(current_dir, 'testfile.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
    time.sleep(10)
    browser.quit