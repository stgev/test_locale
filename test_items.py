from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    btn_cls_name = "btn-add-to-basket"
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, btn_cls_name))
    )
    assert len(browser.find_elements(By.CLASS_NAME, btn_cls_name)) == 1  # selector is unique
