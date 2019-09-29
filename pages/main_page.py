from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    # def go_to_login_page(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    #  в методе, который осуществляет переход к странице логина,
    #  проинициализируем новый объект Page и вернем его
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
