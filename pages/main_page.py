from .locators import BasePageLocators
from .base_page import BasePage


#  заглушка
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
