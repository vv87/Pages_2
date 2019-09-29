from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def go_to_the_shellcoders_handbook_page(self):
        link = self.browser.find_element(*ProductPageLocators.SHELLCODERSHANDBOOK_URL)
        link.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.SUBMIT_BUTTON), "Login link is not presented"
        button = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
        button.click()

    # проверка наличия названия товара в корзине.
    def check_text_book_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.CHECK_TEXT), "Alert of noun name" \
                                                                                      "is not presented"

    # проверка наличия цены товара.
    def check_product_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.CHECK_PRICE), "Alert with price is not presented"

    def success_message_should_be_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.CHECK_SUCCESS_MESSAGE), \
            "Success message is presented, but should has dissapeared"

    def should_be_success_of_addition_message(self):
        name_from_message = self.browser.find_element(*ProductPageLocators.CHECK_SUCCESS_MESSAGE).text
        assert name_from_message == self.get_product_name(), "Name of product and actual product name is not equal"

    def should_be_the_right_price_of_the_cart(self):
        price_of_the_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert price_of_the_cart == self.check_product_price_in_basket(),\
            "Price of product in the cart is not the same as the actual product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CHECK_SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"
