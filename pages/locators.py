from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "header a.btn.btn-default")


class LoginPageLocators(object):
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    SHELLCODERSHANDBOOK_URL = \
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # локатор кнопки "Добавить в корзину"
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    # локатор алерта "Товар добавлен в корзину"
    CHECK_TEXT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner strong")
    # локатор алерта "Цена товара"
    CHECK_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(1) .alertinner strong")
    CHECK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")


class CartPageLocators(object):
    ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".basket-title .col-sm-6")
    NO_ITEMS_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner>p")
