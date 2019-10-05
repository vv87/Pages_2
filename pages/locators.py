from selenium.webdriver.common.by import By


class BasePageLocators(object):
    CART_LINK = (By.CSS_SELECTOR, "header a.btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    EMAIL_FORM = (By.CSS_SELECTOR, "[name='registration-email']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASSWD_FORM_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWD_FORM_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_IN_MESSAGE_OF_SUCCESFUL_ADDITION = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner strong")
    PRICE_OF_THE_CART = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(1) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner")


class CartPageLocators(object):
    ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".basket-title .col-sm-6")
    NO_ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner>p")
