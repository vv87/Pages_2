import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import CartPage


LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_the_cart()
    page.should_be_success_of_addition_message()
    page.should_be_the_right_price_of_the_cart()


@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_see_message_no_products_in_the_cart()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.user_add_to_cart
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "sword123pas"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    @pytest.mark.need_review 
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, LINK)
        page.open()
        page.add_to_the_cart()
        page.should_be_success_of_addition_message()
        page.should_be_the_right_price_of_the_cart()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, LINK)
        page.open()
        page.should_not_be_success_message()