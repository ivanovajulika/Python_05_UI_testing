from selenium.webdriver.common.by import By


class MainPageLocators():
    LINK_TO_PRODUCT_PAGE = (By.XPATH, "//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')
    ADD_BOOK = (By.XPATH, '//*[@id="default"]/div[2]/div/div/div/section/div/ol/li[1]/article/div[2]/form/button')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.XPATH, "//form[@id='register_form']//button")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators():
    FORM_QUANTITY = (By.XPATH, '//*[@id="id_form-0-quantity"]')