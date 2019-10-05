from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_see_message_no_products_in_the_cart(self):
        assert self.is_element_present(*CartPageLocators.NO_ITEMS_IN_CART_MESSAGE), \
        "Message about void cart is not presented, but should be"

    def should_see_no_products_in_the_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_IN_CART_MESSAGE), \
        "Products are presented, but should not be"