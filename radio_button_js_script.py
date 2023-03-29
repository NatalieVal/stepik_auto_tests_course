from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    
    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    #radio_button = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
       
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
