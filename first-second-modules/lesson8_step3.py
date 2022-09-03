from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link =  "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #find sum of num1 and num2
    num1_v = browser.find_element(By.ID, "num1")
    num1 = int(num1_v.text)
    num2_v= browser.find_element(By.ID, "num2")
    num2 = int(num2_v.text)
    sum1 = str(num1+num2)

    #select the value = sum1 in the drop-down list
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(sum1)

    #click submit button
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

