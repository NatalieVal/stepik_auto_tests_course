from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    confirm = browser.switch_to.alert
    confirm.accept()



    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    
    #addToClipBoard = alert_text.split(': ')[-1]
    
    alert.accept()

    print(alert_text.split(': ')[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
