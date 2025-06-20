from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"'login' not found in URL: {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_input1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD1
        )
        password_input2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD2
        )
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)

        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        register_button.click()

    def should_be_login_url(self):
        assert (
            "accounts/login/" in self.browser.current_url
        ), "URL does not contain login path"
