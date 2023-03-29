from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

     # говорим Selenium проверять в течение 12 секунд, пока не появится текст $100
    element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    text_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split(': ')[-1])
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
