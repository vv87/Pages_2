from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()
    page.solve_quiz_and_get_code()  # вызов метода из base_page.py для получения проверочного кода
    page.add_to_basket_button()
    page.solve_quiz_and_get_code()  # запускаем метод в тесте для получения проверочного кода
    page.check_text_book_in_basket()
    page.check_product_price_in_basket()
    page.should_be_success_of_addition_message()
    time.sleep(5)
