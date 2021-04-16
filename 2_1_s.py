from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector('span[id="num1"]').text
    num2 = browser.find_element_by_css_selector('span[id="num2"]').text
    num = int(num2)+int(num1)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("%d"%num)
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла