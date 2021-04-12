import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_autotests_start_for_different_language(browser):
    browser.get(link)
    time.sleep(11)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, 'form[class="add-to-basket"]>button[type="submit"]')
    assert add_to_basket, 'Button "Add to basket" not found.'