from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)

  button = browser.find_element(By.CSS_SELECTOR,'button.btn')
  button.click()

  #first_window = browser.window_handles[0] #имя текущей вкладки, чтобы иметь возможность потом к ней вернуться

  new_window = browser.window_handles[1] #выбираем вторую вкладку
  browser.switch_to.window(new_window)

  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  y = calc(x)

  input1 = browser.find_element(By.ID, 'answer')
  input1.send_keys(y)

  button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
  button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
