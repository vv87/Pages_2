from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()
    page.solve_quiz_and_get_code()  # вызов метода из base_page.py для получения проверочного кода
    page.check_text_book_in_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()
    page.solve_quiz_and_get_code()  # вызов метода из base_page.py для получения проверочного кода
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
