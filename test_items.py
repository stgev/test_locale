from selenium.webdriver.common.by import By


def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    btn_cls_name = "btn-add-to-basket"
    button = browser.find_element(By.CLASS_NAME, btn_cls_name)  # find the button
    assert len(browser.find_elements(By.CLASS_NAME, btn_cls_name)) == 1  # selector is unique
