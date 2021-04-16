from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    f = browser.find_element_by_css_selector('span[id="input_value"]').text
    y = calc(int(f))
    browser.find_element_by_css_selector('input[id="answer"]').send_keys(y)
    browser.find_element_by_css_selector('input[id="robotCheckbox"]').click()
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector('input[id="robotsRule"]').click()
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
