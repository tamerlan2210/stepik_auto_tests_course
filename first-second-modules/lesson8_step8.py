from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input.form-control')
    for element in elements:
        element.send_keys('pohnah')

    choose_file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    choose_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
