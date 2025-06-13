from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import BasePageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Login link is not presented"
