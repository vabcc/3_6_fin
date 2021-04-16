from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    f = browser.find_element_by_css_selector('img[id="treasure"]').get_attribute('valuex')
    y = calc(f)
    browser.find_element_by_css_selector('input[id="answer"]').send_keys(y)
    check = browser.find_element_by_css_selector('input[id="robotCheckbox"]')
    check.click()
    radio = browser.find_element_by_css_selector('input[value="robots"]')
    radio.click()
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла